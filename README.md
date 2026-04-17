# UAI-36-DyAW

Repositorio creado para la Problemática Semanal 01.

## Objetivo

Practicar la vinculación entre un repositorio local y uno remoto en GitHub utilizando Git.

## Datos de la actividad

- Alumno: Nicolas Mastromarino
- Repositorio remoto: `Mastrom10/UAI-36-DyAW`
- Rama principal: `main`

## Comandos Git basicos

- `git clone`: copia un repositorio remoto a la computadora.
- `git add`: prepara archivos para el commit.
- `git commit`: guarda los cambios en el historial local.
- `git push`: sube los commits al repositorio remoto.
- `git pull`: trae los cambios del repositorio remoto.
- `git branch`: muestra o crea ramas.
- `git switch`: cambia de una rama a otra.
- `git merge`: une los cambios de una rama en otra.

## Paso a paso

1. Crear el repositorio remoto en GitHub.
2. Crear el repositorio local.
3. Agregar el archivo `README.md`.
4. Hacer `git add` y `git commit`.
5. Subir la rama `main` con `git push`.
6. Crear una rama secundaria.
7. Modificar el `README.md` en esa rama.
8. Hacer `git add`, `git commit` y `git push`.
9. Crear la Pull Request hacia `main`.
10. Revisar la PR y hacer el merge.

---

## Problemática Semanal 02

### Objetivo

Seleccionar una noticia actual de un diario online, replicar **título, subtítulos y texto** en un documento HTML respetando la **semántica** y el **progreso en GitHub**.

### Noticia y archivo

| Concepto | Detalle |
| -------- | ------- |
| Medio | [BBC News Mundo](https://www.bbc.com/mundo) |
| Título | *Por qué Costa Rica se convirtió en el tercer país de América Latina más endeudado con el FMI después de Argentina y Ecuador* |
| Fecha de publicación | 16 de abril de 2026 |
| Artículo original | [Enlace a la nota en BBC Mundo](https://www.bbc.com/mundo/articles/cz0e9l8vg7jo) |
| Réplica en HTML (práctica) | [`noticia.html`](./noticia.html) |

El HTML resume y organiza fragmentos del artículo con fines educativos; al pie del artículo figura la atribución y el enlace al original.

### Etiquetas semánticas usadas en `noticia.html`

`header`, `main`, `article`, `section`, `aside`, `nav`, `footer`, `figure`, `figcaption`, `h1`, `h2`, `p`, `ol`, `li`, `blockquote`, `cite`, `time`, `abbr`, `a`, `strong`, `em`, `small`, `code`, `span`.

### Flujo Git pedido en la consigna (PS02)

1. Partir de la rama principal `main`.
2. Crear una rama nueva (por ejemplo `feature/ps02-noticia-semantica`) para introducir cambios, incluyendo actualizaciones en este `README.md`.
3. `git push` de la rama y abrir una **Pull Request** hacia `main`.
4. Revisar la PR en GitHub y hacer **merge** a `main`.
5. Entregar en UAI Ultra el **enlace al repositorio**: `https://github.com/Mastrom10/UAI-36-DyAW`

### Pseudocódigo (diseño conceptual — RA1)

```
INICIO
  ELEGIR noticia actual de un diario online (URL y fuente)
  EXTRAER título, subtítulos, párrafos y datos (fecha, autor)
  PLANIFICAR estructura semántica (article, section, aside, etc.)
  CREAR archivo noticia.html con esas etiquetas
  ABRIR noticia.html en el navegador y revisar jerarquía de títulos
  GIT: crear rama desde main → commit → push → PR → merge a main
FIN
```
