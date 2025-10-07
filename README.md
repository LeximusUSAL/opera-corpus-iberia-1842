# 🎭 Análisis del Corpus de Ópera - Revista Iberia (1842)

## 📋 Descripción del Proyecto

Análisis exhaustivo palabra por palabra de **34 números digitalizados** de la **Revista Iberia** publicados en 1842, centrados en el contenido operístico. Este proyecto de Humanidades Digitales aplica técnicas de procesamiento de lenguaje natural (NLP) para extraer y visualizar patrones en el discurso crítico musical del romanticismo español.

**🌐 Ver el análisis completo:** [https://leximususal.github.io/opera-corpus-iberia-1842/](https://leximususal.github.io/opera-corpus-iberia-1842/)

---

## 📊 Estadísticas del Corpus

| Métrica | Valor |
|---------|-------|
| **Archivos procesados** | 34 números de revista |
| **Total de palabras** | 72,933 |
| **Palabras únicas** | 9,737 |
| **Período cubierto** | Enero-Agosto 1842 |
| **Compositores identificados** | 24 |
| **Cantantes identificados** | 14 |

---

## 🎼 Principales Hallazgos

### Compositores Más Citados (Top 5)

1. **Rossini** - 78 menciones
2. **Meyerbeer** - 52 menciones
3. **Donizetti** - 46 menciones
4. **Mozart** - 28 menciones
5. **Mercadante** - 23 menciones

### Cantantes Más Mencionados (Top 5)

1. **Rubini** (tenor) - 76 menciones
2. **Malibran** (soprano) - 25 menciones
3. **Lablache** (bajo) - 16 menciones
4. **Saldoni** - 14 menciones
5. **Tamburini** (barítono) - 10 menciones

### Léxico Musical - Categorías Principales

| Categoría | Menciones |
|-----------|-----------|
| **Voces** | 701 |
| **Elementos escénicos** | 565 |
| **Formas musicales** | 555 |
| **Expresión musical** | 543 |
| **Términos técnicos** | 469 |
| **Géneros operísticos** | 417 |
| **Crítica y opinión** | 431 |

---

## 🔍 Interpretación Histórico-Cultural

### Hegemonía del Repertorio Italiano

El análisis revela la **dominación absoluta del repertorio italiano** en Madrid en 1842, con Rossini como figura central (78 menciones). El *bel canto* (Donizetti, Bellini) y la *opera seria* rossiniana constituyen el núcleo del repertorio.

### Influencia de la Grand Opéra Francesa

**Meyerbeer** (52 menciones) representa la penetración de la *grand opéra* francesa en España, con su espectacularidad escénica y dramaturgia histórica.

### Centralidad de los Intérpretes

**Rubini** (76 menciones) y **Malibran** (25 menciones) demuestran que los cantantes eran tan importantes como los compositores. La figura del **divo** operístico domina la recepción crítica.

### Público Conocedor

El vocabulario técnico especializado (armonía, modulación, coloratura, fioritura) evidencia una **audiencia cultivada** y una **crítica musical profesional**.

### Teatros como Centros Culturales

Los teatros madrileños (**Teatro del Príncipe**, **Teatro de la Cruz**) aparecen como espacios centrales de sociabilidad cultural y debate estético.

---

## 🛠️ Metodología

### 1. Unificación del Corpus
- Combinación de 34 archivos `.txt` sin pérdida de información
- Normalización Unicode (NFC)
- Eliminación de duplicados

### 2. Procesamiento NLP
- Análisis palabra por palabra con expresiones regulares
- Tokenización y conteo de frecuencias
- Extracción de bigramas y trigramas

### 3. Identificación de Entidades
- **Compositores**: 24 figuras del repertorio operístico 1750-1850
- **Cantantes**: 14 intérpretes líricos de fama internacional
- **Léxico musical**: 150+ términos clasificados en 8 categorías

### 4. Análisis Estadístico
- Frecuencias absolutas y relativas
- Distribuciones por categorías
- Coocurrencias y colocaciones frecuentes

### 5. Visualización Interactiva
- Gráficos dinámicos con **Chart.js**
- Tablas comparativas con porcentajes
- Interpretaciones cualitativas contextualizadas

---

## 📁 Estructura del Proyecto

```
opera-corpus-iberia-1842/
│
├── index.html                                      # Web interactiva con visualizaciones
├── resultados_analisis_opera_iberia_1842.json     # Datos completos del análisis
├── analizador_corpus_opera.py                     # Script de análisis en Python
└── README.md                                       # Documentación del proyecto
```

---

## 🚀 Uso del Script de Análisis

### Requisitos
- Python 3.7+
- Módulos estándar: `re`, `json`, `collections`, `pathlib`, `unicodedata`

### Ejecución

```bash
python3 analizador_corpus_opera.py
```

El script genera:
- `resultados_analisis_opera_iberia_1842.json` - Datos estructurados
- Resumen en consola con estadísticas principales

---

## 📖 Categorías del Léxico Musical

### Géneros Operísticos
Ópera, melodrama, ópera seria, ópera bufa, ópera cómica, zarzuela, tonadilla

### Voces
Soprano, contralto, mezzo-soprano, tenor, barítono, bajo, prima donna

### Técnica Vocal
Aria, cavatina, cabaletta, recitativo, bel canto, coloratura, agilidad, trino, cadencia

### Formas Musicales
Acto, escena, obertura, preludio, dúo, terceto, cuarteto, coro

### Elementos Escénicos
Teatro, escenario, decoración, vestuario, tramoya, función, espectáculo

### Expresión Musical
Sublime, patético, brillante, gracia, elegancia, inspiración, genio, mérito

### Términos Técnicos
Partitura, melodía, armonía, orquesta, tonalidad, modulación, ritmo, compás

### Crítica y Opinión
Aplauso, éxito, triunfo, ovación, crítica, juicio, público, mérito

---

## 🎯 Conclusiones Generales

1. **Internacionalización del gusto musical** español en el período romántico
2. **Hegemonía italiana** en compositores e intérpretes
3. **Profesionalización de la crítica musical** en la prensa periódica
4. **Importancia social del teatro** como centro de vida cultural
5. **Público conocedor** con vocabulario técnico especializado
6. **Equilibrio entre obra y ejecución** en el juicio crítico
7. **Tensión entre repertorio extranjero y aspiraciones de ópera nacional**

---

## 🏛️ Contexto Académico

Este proyecto se enmarca en el estudio de la **recepción de la ópera en España** durante el siglo XIX, contribuyendo al análisis de:

- Formación del canon operístico español
- Circulación de repertorios internacionales
- Desarrollo del periodismo musical especializado
- Gusto musical de las clases urbanas ilustradas
- Construcción de identidades musicales nacionales

**Proyecto relacionado:** *LexiMus: Léxico y ontología de la música en español* (PID2022-139589NB-C33)
**Instituciones:** Universidad de Salamanca, Instituto Complutense de Ciencias Musicales, Universidad de La Rioja

---

## 📜 Licencia

Este proyecto utiliza fuentes históricas de dominio público (Revista Iberia, 1842).
El código de análisis y la web están disponibles para uso académico.

---

## 👤 Autores

**Análisis y procesamiento:** LexiMus (Universidad de Salamanca)
**Generado con:** Claude Code (Anthropic)

---

## 🔗 Enlaces

- **Web del proyecto:** [https://leximususal.github.io/inicio/)
- **Repositorio GitHub:** [https://github.com/LeximusUSAL/opera-corpus-iberia-1842](https://github.com/LeximusUSAL/opera-corpus-iberia-1842)
- **Proyecto LexiMus:** Universidad de Salamanca

---

**Fecha de análisis:** Octubre 2025
**Versión:** 1.0
