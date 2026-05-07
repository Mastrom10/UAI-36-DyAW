# Clase 4 — Actividad (TP1: Selectores y layout)

## Objetivo

Implementar una réplica HTML/CSS de una noticia de un diario online usando **hoja de estilos externa**, **selectores** y **layout**, con elementos semánticos y referencia explícita al original para que los tutores puedan comparar.

## Noticia original

| Campo | Valor |
| ----- | ----- |
| Medio | [BBC News Mundo](https://www.bbc.com/mundo) |
| Título | *Los efectos para el cuerpo de pasar muchas horas sentado y cómo puedes combatirlos* |
| URL del artículo original | **https://www.bbc.com/mundo/articles/c9v3y03x3rmo** |

> La fuente del texto en la versión de BBC es **The Conversation** (republicación con licencia Creative Commons), según el propio artículo.

## Archivos de la entrega

| Archivo | Descripción |
| ------- | ----------- |
| [`noticia.html`](./noticia.html) | Documento HTML semántico (`header`, `main`, `article`, `section`, `figure`, `aside`, `nav`, `footer`, etc.). |
| [`styles.css`](./styles.css) | Estilos: selectores de clase, layout de columna estilo artículo, tipografía y cabecera tipo marca. |
| [`serve.py`](./serve.py) | Servidor HTTP local (puerto **8084**) para previsualizar la carpeta. |

### Vista local

Desde esta carpeta:

```bash
python3 serve.py
```

Abrir en el navegador: `http://127.0.0.1:8084/noticia.html`

## Pseudocódigo — diseño conceptual del documento (RA1)

```
INICIO
  ELEGIR noticia actual en diario online y registrar su URL en README
  PLANIFICAR estructura semántica (cabecera de marca, article, secciones, figuras, aside)
  CREAR noticia.html con contenido fiel al original y rutas a imágenes públicas de la misma fuente
  CREAR styles.css con selectores reutilizables (.site-header, .article-body, .section-title, etc.)
  REVISAR contraste jerárquico (h1, h2, párrafos, figcaption)
  GIT add / commit / push al repositorio de la materia
FIN
```
