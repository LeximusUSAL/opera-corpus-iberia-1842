# 📘 INSTRUCCIONES DE USO - Análisis Corpus de Ópera

## 🌐 Acceso a la Web Interactiva

### URL Principal
**https://leximususal.github.io/opera-corpus-iberia-1842/**

Abre esta URL en cualquier navegador moderno (Chrome, Firefox, Safari, Edge) para acceder al dashboard completo con todas las visualizaciones interactivas.

---

## 📊 Navegación por la Web

### Secciones Disponibles

1. **Banner de Estadísticas** (parte superior)
   - Archivos procesados
   - Total de palabras
   - Palabras únicas
   - Compositores citados

2. **Compositores Más Citados**
   - Gráfico de barras horizontal (Top 15)
   - Tabla completa con frecuencias y porcentajes
   - Interpretación contextualizada

3. **Cantantes Más Mencionados**
   - Gráfico circular (Top 10)
   - Tabla con barras de frecuencia visual
   - Análisis de roles vocales

4. **Léxico Musical Operístico**
   - Gráfico de categorías generales
   - Gráficos específicos (géneros, voces)
   - Análisis del vocabulario especializado

5. **Temas Principales**
   - Distribución temática
   - Nube de etiquetas interactiva
   - Contexto histórico-cultural

6. **Palabras Más Frecuentes**
   - Top 30 palabras (sin stopwords)
   - Visualización por frecuencia

7. **Colocaciones Frecuentes**
   - Bigramas (pares de palabras)
   - Trigramas (tres palabras)
   - Análisis de expresiones formulaicas

8. **Metodología**
   - Proceso de análisis detallado
   - Criterios de calidad
   - Rigor académico

9. **Conclusiones Generales**
   - Hallazgos principales
   - Significado histórico-cultural
   - Interpretación final

### Interactividad

- **Gráficos**: Pasa el mouse sobre cualquier elemento para ver valores exactos
- **Tablas**: Todas las tablas muestran rankings y frecuencias precisas
- **Etiquetas**: En la sección de temas, las etiquetas son interactivas (hover para efectos)
- **Scroll suave**: La página tiene animaciones de aparición progresiva

---

## 🖥️ Uso del Script de Análisis Python

### Ubicación
`/Users/maria/analizador_corpus_opera.py`

### Requisitos
- **Python 3.7+**
- Módulos estándar (incluidos en Python):
  - `re` (expresiones regulares)
  - `json` (manejo de JSON)
  - `collections` (Counter, defaultdict)
  - `pathlib` (gestión de rutas)
  - `unicodedata` (normalización Unicode)

### Ejecución

```bash
cd /Users/maria
python3 analizador_corpus_opera.py
```

### Salida del Script

El script genera:

1. **Consola:**
   - Progreso de procesamiento archivo por archivo
   - Resumen interpretativo completo
   - Estadísticas principales

2. **Archivo JSON:**
   - `resultados_analisis_opera_iberia_1842.json`
   - Contiene todos los datos estructurados
   - Formato legible para humanos y máquinas

### Modificar el Directorio de Entrada

Edita la línea 373 del script:

```python
directorio_corpus = "/Users/maria/Desktop/RESULTADOS ÓPERA TXT"
```

Cambia esta ruta si tus archivos .txt están en otra ubicación.

---

## 📂 Estructura de Archivos Generados

### En `/Users/maria/`

```
maria/
├── analizador_corpus_opera.py                    # Script de análisis
├── resultados_analisis_opera_iberia_1842.json   # Datos completos
├── index.html                                    # Web interactiva
├── README.md                                     # Documentación
├── RESUMEN_ANALISIS_OPERA.md                    # Resumen ejecutivo
└── INSTRUCCIONES_USO.md                         # Este archivo
```

### En GitHub

**Repositorio:** https://github.com/LeximusUSAL/opera-corpus-iberia-1842

- Todos los archivos listados arriba están sincronizados
- GitHub Pages se genera automáticamente desde `index.html`

---

## 🔄 Actualizar el Análisis

### Si Cambias los Datos Fuente

1. **Ejecuta el script nuevamente:**
   ```bash
   python3 analizador_corpus_opera.py
   ```

2. **Actualiza Git:**
   ```bash
   cd /Users/maria
   git add resultados_analisis_opera_iberia_1842.json
   git commit -m "Actualizar datos del análisis"
   git push origin main
   ```

3. **Espera 1-2 minutos** para que GitHub Pages se actualice automáticamente.

### Si Modificas la Web (index.html)

1. **Edita el archivo:**
   ```bash
   # Usa tu editor preferido
   open -a "TextEdit" index.html
   ```

2. **Prueba localmente** (abre en navegador):
   ```bash
   open index.html
   ```

3. **Sube cambios a GitHub:**
   ```bash
   git add index.html
   git commit -m "Actualizar diseño web"
   git push origin main
   ```

---

## 📊 Interpretar los Datos JSON

### Estructura del JSON

```json
{
  "metadata": {
    "titulo": "...",
    "fecha_analisis": "2025-10-07",
    "archivos_procesados": 34,
    "total_palabras": 72933,
    "palabras_unicas": 9737
  },
  "compositores": {
    "Rossini": 78,
    "Meyerbeer": 52,
    ...
  },
  "cantantes": {
    "Rubini": 76,
    "Malibran": 25,
    ...
  },
  "lexico_musical": {
    "generos_operisticos": {...},
    "voces": {...},
    ...
  },
  "temas_principales": {...},
  "palabras_frecuentes": {...},
  "colocaciones": {
    "bigramas_top": {...},
    "trigramas_top": {...}
  },
  "archivos": [...]
}
```

### Acceso Programático

```python
import json

with open('resultados_analisis_opera_iberia_1842.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Ejemplo: Top 5 compositores
top5 = list(datos['compositores'].items())[:5]
for compositor, menciones in top5:
    print(f"{compositor}: {menciones} menciones")
```

---

## 🎨 Personalizar el Diseño Web

### Colores Principales (CSS variables en `<style>`)

```css
--primary-color: #8B0000;    /* Rojo oscuro operístico */
--secondary-color: #FFD700;  /* Dorado elegante */
--background: #0a0a0a;       /* Negro profundo */
--card-bg: #1a1a1a;          /* Gris oscuro para tarjetas */
--text: #e0e0e0;             /* Texto claro */
--accent: #CD853F;           /* Acento dorado-marrón */
```

### Modificar Gráficos

Los gráficos usan **Chart.js 4.4.0**. Busca las funciones `crear*` en el `<script>` al final del HTML:

- `crearGraficoCompositores()` - Gráfico de barras de compositores
- `crearGraficoCantantes()` - Gráfico circular de cantantes
- `crearGraficoLexicoCategorias()` - Categorías de léxico
- etc.

Documentación de Chart.js: https://www.chartjs.org/docs/latest/

---

## 🐛 Solución de Problemas

### La web no carga los datos

**Problema:** La web muestra "0" en todas las estadísticas.

**Solución:**
1. Verifica que `resultados_analisis_opera_iberia_1842.json` esté en la misma carpeta que `index.html`
2. Abre la consola del navegador (F12) y busca errores
3. Comprueba que el JSON sea válido: https://jsonlint.com/

### El script Python falla

**Problema:** Error al ejecutar el script.

**Soluciones comunes:**
- Verifica la ruta del directorio (línea 373)
- Asegúrate de que los archivos .txt existan
- Comprueba permisos de lectura:
  ```bash
  ls -la "/Users/maria/Desktop/RESULTADOS ÓPERA TXT"
  ```

### GitHub Pages no actualiza

**Problema:** Los cambios no se reflejan en la web.

**Soluciones:**
1. Espera 1-2 minutos (puede tardar)
2. Limpia caché del navegador (Cmd+Shift+R en Mac)
3. Verifica que el push fue exitoso:
   ```bash
   git log --oneline -5
   ```
4. Comprueba el estado de Pages en:
   https://github.com/LeximusUSAL/opera-corpus-iberia-1842/settings/pages

---

## 📚 Recursos Adicionales

### Archivos de Documentación

1. **README.md** - Descripción general del proyecto
2. **RESUMEN_ANALISIS_OPERA.md** - Análisis detallado con todos los hallazgos
3. **INSTRUCCIONES_USO.md** - Este archivo (guía práctica)

### Enlaces Útiles

- **Web del proyecto:** https://leximususal.github.io/opera-corpus-iberia-1842/
- **Repositorio GitHub:** https://github.com/LeximusUSAL/opera-corpus-iberia-1842
- **Chart.js Docs:** https://www.chartjs.org/
- **Markdown Guide:** https://www.markdownguide.org/

---

## 🎯 Casos de Uso

### Para Investigadores

1. **Consultar frecuencias exactas:** Abre `resultados_analisis_opera_iberia_1842.json`
2. **Ver contexto histórico:** Lee `RESUMEN_ANALISIS_OPERA.md`
3. **Citar el proyecto:** Usa el DOI o URL del repositorio GitHub

### Para Estudiantes

1. **Explorar visualizaciones:** Navega por la web interactiva
2. **Leer interpretaciones:** Cada sección tiene cuadros interpretativos
3. **Aprender metodología:** Revisa la sección "Metodología" en la web

### Para Desarrolladores

1. **Reusar el código:** El script Python es modular y adaptable
2. **Modificar visualizaciones:** Edita las funciones de Chart.js
3. **Extender el análisis:** Añade nuevas categorías al diccionario `lexico_musical`

---

## ✉️ Contacto y Soporte

### Proyecto Académico

**LexiMus: Léxico y ontología de la música en español**
- Código: PID2022-139589NB-C33
- Universidad de Salamanca
- Instituto Complutense de Ciencias Musicales
- Universidad de La Rioja

### Issues de GitHub

Si encuentras problemas o tienes sugerencias, abre un issue en:
https://github.com/LeximusUSAL/opera-corpus-iberia-1842/issues

---

## 📜 Licencia

Este proyecto utiliza fuentes históricas de dominio público (Revista Iberia, 1842).
El código de análisis y la web están disponibles para uso académico.

---

## 🎭 Cita Sugerida

```
María. (2025). Análisis del Corpus de Ópera - Revista Iberia (1842).
GitHub. https://github.com/LeximusUSAL/opera-corpus-iberia-1842
```

---

**Última actualización:** 7 de octubre de 2025
**Versión:** 1.0
**Generado con:** Claude Code (Anthropic)

---

🎵 *"La música es el arte más directo, entra por el oído y va al corazón"* — Revista Iberia, 1842
