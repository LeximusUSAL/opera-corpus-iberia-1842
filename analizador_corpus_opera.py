#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analizador Exhaustivo del Corpus de Ópera - Revista Iberia (1842)
Análisis palabra por palabra de 34 archivos de texto sobre ópera
"""

import os
import re
import json
from collections import Counter, defaultdict
from pathlib import Path
import unicodedata

class AnalizadorCorpusOpera:
    """Procesador exhaustivo del corpus de ópera"""

    def __init__(self, directorio_base):
        self.directorio_base = directorio_base
        self.corpus_completo = []
        self.textos_por_archivo = {}
        self.estadisticas = {
            'total_palabras': 0,
            'total_archivos': 0,
            'palabras_unicas': 0
        }

        # Compositores de ópera del siglo XIX y anteriores (búsqueda exhaustiva)
        self.compositores = {
            # Compositores italianos
            'Rossini': ['Rossini', 'Rosini', 'Gioachino Rossini'],
            'Donizetti': ['Donizetti', 'Gaetano Donizetti', 'Donizeti'],
            'Bellini': ['Bellini', 'Vincenzo Bellini'],
            'Verdi': ['Verdi', 'Giuseppe Verdi'],
            'Pacini': ['Pacini', 'Giovanni Pacini'],
            'Mercadante': ['Mercadante', 'Saverio Mercadante'],
            'Pergolesi': ['Pergolesi', 'Giovanni Battista Pergolesi'],
            'Cimarosa': ['Cimarosa', 'Domenico Cimarosa'],
            'Paisiello': ['Paisiello', 'Giovanni Paisiello'],
            'Spontini': ['Spontini', 'Gaspare Spontini'],
            'Cherubini': ['Cherubini', 'Luigi Cherubini'],

            # Compositores franceses
            'Meyerbeer': ['Meyerbeer', 'Giacomo Meyerbeer', 'Meyer-Beer'],
            'Auber': ['Auber', 'Daniel Auber'],
            'Halévy': ['Halévy', 'Fromental Halévy', 'Halevy'],
            'Boieldieu': ['Boieldieu', 'François-Adrien Boieldieu'],
            'Hérold': ['Hérold', 'Ferdinand Hérold', 'Herold'],
            'Adam': ['Adam', 'Adolphe Adam'],

            # Compositores alemanes
            'Mozart': ['Mozart', 'Wolfgang Amadeus Mozart', 'W. A. Mozart'],
            'Weber': ['Weber', 'Carl Maria von Weber'],
            'Gluck': ['Gluck', 'Christoph Willibald Gluck'],

            # Compositores españoles
            'Carnicer': ['Carnicer', 'Ramón Carnicer'],
            'Saldoni': ['Saldoni', 'Baltasar Saldoni'],
            'Oudrid': ['Oudrid', 'Cristóbal Oudrid'],
            'Eslava': ['Eslava', 'Hilarión Eslava']
        }

        # Cantantes de ópera del siglo XIX (cantantes líricos famosos)
        self.cantantes = {
            # Sopranos
            'Malibran': ['Malibran', 'María Malibran', 'Malibrán'],
            'Pasta': ['Pasta', 'Giuditta Pasta'],
            'Grisi': ['Grisi', 'Giulia Grisi'],
            'Persiani': ['Persiani', 'Fanny Persiani'],
            'Castellan': ['Castellan', 'Jeanne-Anaïs Castellan'],
            'Albertazzi': ['Albertazzi', 'Emma Albertazzi'],

            # Tenores
            'Rubini': ['Rubini', 'Giovanni Battista Rubini'],
            'Donzelli': ['Donzelli', 'Domenico Donzelli'],
            'Moriani': ['Moriani', 'Napoleone Moriani'],
            'Ivanoff': ['Ivanoff', 'Nicolai Ivanoff', 'Ivanof'],

            # Barítonos y bajos
            'Tamburini': ['Tamburini', 'Antonio Tamburini'],
            'Lablache': ['Lablache', 'Luigi Lablache'],
            'Ronconi': ['Ronconi', 'Giorgio Ronconi'],
            'Galli': ['Galli', 'Filippo Galli'],

            # Cantantes españoles
            'Saldoni': ['Saldoni', 'Baltasar Saldoni'],
            'Monjo': ['Monjo', 'Joaquín Monjo'],
            'Albini': ['Albini'],
            'Blasco': ['Blasco']
        }

        # Léxico musical operístico - Clasificación exhaustiva
        self.lexico_musical = {
            'generos_operisticos': [
                'ópera', 'opera', 'melodrama', 'dramma', 'drama lírico',
                'ópera seria', 'ópera bufa', 'ópera cómica', 'opereta',
                'zarzuela', 'tonadilla', 'sainete lírico'
            ],
            'voces': [
                'soprano', 'contralto', 'mezzosoprano', 'mezzo-soprano',
                'tenor', 'barítono', 'bajo', 'basso', 'tiple',
                'voz', 'canto', 'cantante', 'cantatriz', 'prima donna',
                'comprimario', 'coro', 'corista'
            ],
            'tecnica_vocal': [
                'aria', 'cavatina', 'cabaletta', 'romanza', 'recitativo',
                'bel canto', 'coloratura', 'agilidad', 'fioritura', 'trino',
                'cadencia', 'portamento', 'legato', 'staccato',
                'messa di voce', 'registro', 'agudo', 'grave',
                'falsete', 'pecho', 'cabeza', 'timbre', 'tesitura'
            ],
            'formas_musicales': [
                'acto', 'escena', 'cuadro', 'obertura', 'preludio',
                'intermedio', 'sinfonía', 'introducción', 'final',
                'dúo', 'terceto', 'cuarteto', 'conjunto', 'concertante',
                'coro', 'solo', 'recitado'
            ],
            'elementos_escenico': [
                'escena', 'teatro', 'tablado', 'escenario', 'decoración',
                'vestuario', 'tramoya', 'telón', 'bastidor',
                'representación', 'función', 'espectáculo',
                'actor', 'actriz', 'papel', 'personaje', 'protagonista'
            ],
            'expresion_musical': [
                'expresión', 'sentimiento', 'pasión', 'emoción', 'afecto',
                'sublime', 'patético', 'brillante', 'maestría', 'gracia',
                'elegancia', 'gusto', 'estilo', 'carácter', 'efecto',
                'inspiración', 'genio', 'talento', 'mérito'
            ],
            'terminos_tecnicos': [
                'partitura', 'composición', 'música', 'melodía', 'armonía',
                'orquesta', 'instrumentación', 'acompañamiento',
                'motivo', 'tema', 'frase', 'periodo',
                'tonalidad', 'modulación', 'acorde', 'ritmo', 'compás',
                'tiempo', 'andante', 'allegro', 'adagio', 'presto'
            ],
            'critica_opinion': [
                'aplauso', 'éxito', 'triunfo', 'ovación', 'aclamación',
                'crítica', 'juicio', 'opinión', 'público', 'auditorio',
                'inteligente', 'dilettante', 'aficionado', 'conocedor',
                'mérito', 'defecto', 'belleza', 'perfección'
            ]
        }

        # Temas principales para análisis de contenido
        self.temas = {
            'teatros': ['teatro', 'coliseo', 'liceo', 'cruz', 'príncipe', 'real'],
            'estrenos': ['estreno', 'debut', 'primera vez', 'nueva ópera', 'novedad'],
            'critica': ['crítica', 'juicio', 'opinión', 'censura', 'elogio'],
            'publico': ['público', 'auditorio', 'concurrencia', 'espectadores'],
            'interpretacion': ['ejecución', 'desempeño', 'interpretación', 'canto'],
            'composicion': ['composición', 'obra', 'partitura', 'música'],
            'nacionalidad': ['italiano', 'italiana', 'español', 'española', 'francés', 'francesa', 'alemán', 'alemana']
        }

    def normalizar_texto(self, texto):
        """Normaliza texto manteniendo acentos pero estandarizando formato"""
        texto = unicodedata.normalize('NFC', texto)
        return texto

    def leer_corpus_completo(self):
        """Lee todos los archivos .txt del directorio y construye el corpus unificado"""
        print(f"📚 Leyendo corpus desde: {self.directorio_base}")

        archivos_txt = sorted(Path(self.directorio_base).glob('*.txt'))
        self.estadisticas['total_archivos'] = len(archivos_txt)

        corpus_texto_completo = []

        for archivo in archivos_txt:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    contenido_normalizado = self.normalizar_texto(contenido)

                    # Almacenar por archivo
                    self.textos_por_archivo[archivo.name] = contenido_normalizado

                    # Añadir al corpus completo
                    corpus_texto_completo.append(contenido_normalizado)

                    # Contar palabras
                    palabras = re.findall(r'\b\w+\b', contenido_normalizado.lower())
                    self.estadisticas['total_palabras'] += len(palabras)

                print(f"✓ Procesado: {archivo.name}")
            except Exception as e:
                print(f"✗ Error en {archivo.name}: {e}")

        # Unificar corpus
        self.corpus_completo = '\n\n'.join(corpus_texto_completo)

        # Palabras únicas
        todas_palabras = re.findall(r'\b\w+\b', self.corpus_completo.lower())
        self.estadisticas['palabras_unicas'] = len(set(todas_palabras))

        print(f"\n✅ Corpus unificado: {self.estadisticas['total_archivos']} archivos")
        print(f"   Total palabras: {self.estadisticas['total_palabras']:,}")
        print(f"   Palabras únicas: {self.estadisticas['palabras_unicas']:,}")

    def buscar_menciones(self, patrones, texto=None):
        """Busca y cuenta menciones de una lista de patrones"""
        if texto is None:
            texto = self.corpus_completo

        contador = Counter()

        for nombre_principal, variantes in patrones.items():
            total_menciones = 0
            for variante in variantes:
                # Búsqueda insensible a mayúsculas
                patron = re.compile(r'\b' + re.escape(variante) + r'\b', re.IGNORECASE)
                menciones = len(patron.findall(texto))
                total_menciones += menciones

            if total_menciones > 0:
                contador[nombre_principal] = total_menciones

        return contador

    def analizar_compositores(self):
        """Analiza compositores más citados con frecuencias exactas"""
        print("\n🎼 Analizando compositores...")
        return self.buscar_menciones(self.compositores)

    def analizar_cantantes(self):
        """Analiza cantantes más mencionados con frecuencias"""
        print("🎤 Analizando cantantes...")
        return self.buscar_menciones(self.cantantes)

    def analizar_lexico_musical(self):
        """Extrae y clasifica léxico musical operístico"""
        print("📖 Analizando léxico musical...")

        resultados_lexico = {}

        for categoria, terminos in self.lexico_musical.items():
            contador = Counter()
            for termino in terminos:
                patron = re.compile(r'\b' + re.escape(termino) + r'\b', re.IGNORECASE)
                menciones = len(patron.findall(self.corpus_completo))
                if menciones > 0:
                    contador[termino] = menciones

            resultados_lexico[categoria] = dict(contador.most_common(30))

        return resultados_lexico

    def analizar_temas_principales(self):
        """Identifica temas principales recurrentes"""
        print("📊 Analizando temas principales...")

        resultados_temas = {}

        for tema, palabras_clave in self.temas.items():
            contador = Counter()
            for palabra in palabras_clave:
                patron = re.compile(r'\b' + re.escape(palabra) + r'\b', re.IGNORECASE)
                menciones = len(patron.findall(self.corpus_completo))
                if menciones > 0:
                    contador[palabra] = menciones

            resultados_temas[tema] = dict(contador)

        return resultados_temas

    def extraer_bigramas_trigramas(self):
        """Extrae colocaciones frecuentes (bigramas y trigramas)"""
        print("🔗 Extrayendo colocaciones frecuentes...")

        palabras = re.findall(r'\b\w+\b', self.corpus_completo.lower())

        # Bigramas
        bigramas = []
        for i in range(len(palabras) - 1):
            if len(palabras[i]) > 3 and len(palabras[i+1]) > 3:
                bigramas.append(f"{palabras[i]} {palabras[i+1]}")

        # Trigramas
        trigramas = []
        for i in range(len(palabras) - 2):
            if len(palabras[i]) > 3 and len(palabras[i+1]) > 3 and len(palabras[i+2]) > 3:
                trigramas.append(f"{palabras[i]} {palabras[i+1]} {palabras[i+2]}")

        return {
            'bigramas_top': dict(Counter(bigramas).most_common(50)),
            'trigramas_top': dict(Counter(trigramas).most_common(50))
        }

    def generar_analisis_completo(self):
        """Ejecuta análisis completo y retorna todos los resultados"""
        print("\n" + "="*70)
        print("🎭 ANÁLISIS EXHAUSTIVO DEL CORPUS DE ÓPERA - IBERIA 1842")
        print("="*70)

        # Leer corpus
        self.leer_corpus_completo()

        # Análisis de entidades
        compositores = self.analizar_compositores()
        cantantes = self.analizar_cantantes()
        lexico = self.analizar_lexico_musical()
        temas = self.analizar_temas_principales()
        colocaciones = self.extraer_bigramas_trigramas()

        # Palabras más frecuentes (filtradas)
        print("📈 Calculando palabras más frecuentes...")
        stopwords = {'de', 'la', 'el', 'en', 'y', 'a', 'que', 'del', 'las', 'los',
                     'se', 'con', 'por', 'para', 'una', 'un', 'al', 'su', 'ha', 'lo',
                     'es', 'le', 'como', 'más', 'no', 'muy', 'ya', 'este', 'esta'}

        palabras = re.findall(r'\b\w+\b', self.corpus_completo.lower())
        palabras_filtradas = [p for p in palabras if p not in stopwords and len(p) > 3]
        palabras_frecuentes = dict(Counter(palabras_filtradas).most_common(100))

        # Preparar resultados
        resultados = {
            'metadata': {
                'titulo': 'Análisis Exhaustivo del Corpus de Ópera - Revista Iberia (1842)',
                'fecha_analisis': '2025-10-07',
                'archivos_procesados': self.estadisticas['total_archivos'],
                'total_palabras': self.estadisticas['total_palabras'],
                'palabras_unicas': self.estadisticas['palabras_unicas']
            },
            'compositores': dict(compositores.most_common(30)),
            'cantantes': dict(cantantes.most_common(30)),
            'lexico_musical': lexico,
            'temas_principales': temas,
            'palabras_frecuentes': palabras_frecuentes,
            'colocaciones': colocaciones,
            'archivos': list(self.textos_por_archivo.keys())
        }

        return resultados

    def guardar_resultados_json(self, resultados, archivo_salida):
        """Guarda resultados en formato JSON"""
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Resultados guardados en: {archivo_salida}")

    def imprimir_resumen(self, resultados):
        """Imprime resumen interpretativo de resultados"""
        print("\n" + "="*70)
        print("📊 RESUMEN INTERPRETATIVO DE RESULTADOS")
        print("="*70)

        print(f"\n📚 CORPUS:")
        print(f"   • {resultados['metadata']['archivos_procesados']} archivos analizados")
        print(f"   • {resultados['metadata']['total_palabras']:,} palabras totales")
        print(f"   • {resultados['metadata']['palabras_unicas']:,} palabras únicas")

        print(f"\n🎼 COMPOSITORES MÁS CITADOS (Top 10):")
        for i, (compositor, menciones) in enumerate(list(resultados['compositores'].items())[:10], 1):
            print(f"   {i:2d}. {compositor:20s} → {menciones:4d} menciones")

        print(f"\n🎤 CANTANTES MÁS MENCIONADOS (Top 10):")
        for i, (cantante, menciones) in enumerate(list(resultados['cantantes'].items())[:10], 1):
            print(f"   {i:2d}. {cantante:20s} → {menciones:4d} menciones")

        print(f"\n📖 LÉXICO MUSICAL - CATEGORÍAS:")
        for categoria, terminos in resultados['lexico_musical'].items():
            total_menciones = sum(terminos.values())
            print(f"   • {categoria:25s}: {total_menciones:5d} menciones")

        print(f"\n📊 TEMAS PRINCIPALES:")
        for tema, palabras in resultados['temas_principales'].items():
            total = sum(palabras.values())
            print(f"   • {tema:20s}: {total:4d} menciones")

        print("\n" + "="*70)


def main():
    """Función principal"""
    # Configurar directorio
    directorio_corpus = "/Users/maria/Desktop/RESULTADOS ÓPERA TXT"

    # Crear analizador
    analizador = AnalizadorCorpusOpera(directorio_corpus)

    # Ejecutar análisis completo
    resultados = analizador.generar_analisis_completo()

    # Guardar resultados
    archivo_json = "/Users/maria/resultados_analisis_opera_iberia_1842.json"
    analizador.guardar_resultados_json(resultados, archivo_json)

    # Imprimir resumen
    analizador.imprimir_resumen(resultados)

    print("\n✅ Análisis completado exitosamente")
    return resultados


if __name__ == "__main__":
    main()
