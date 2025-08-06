# CRUD-CURSOS-ONLINE
##  Catálogo de Cursos Online

Este es un proyecto desarrollado en equipo aplicando **Scrum + XP**. Consiste en una plataforma web para visualizar, registrar, actualizar y eliminar cursos. Se utilizó el framework Django, y se integraron buenas prácticas de desarrollo ágil como control de versiones con GitHub, integración continua (CI), pruebas automatizadas y colaboración en Trello.

##  Instalación y Ejecución Local

### Requisitos Previos

- Python 3.8 o superior  
- Pip (gestor de paquetes de Python)  
- Git (opcional para clonar el repositorio)

### Instalación

1. Clona el repositorio:
- git clone https://github.com/Jorgehuillca/CRUD-CURSOS-ONLINE.git
- cd CRUD-CURSOS-ONLINE

2. Instala las dependencias:
- pip install -r requirements.txt

3. Aplica las migraciones de la base de datos:
- python manage.py migrate

4. Recolecta archivos estáticos:
- python manage.py collectstatic --no-input

5. Ejecuta el servidor de desarrollo local:
- python manage.py runserver

6. Accede a la aplicación en tu navegador:
- http://localhost:8000/ <-- Solo es un ejemplo, tu dirección es distinta

---------------------------------------------

### Roles

| Integrante     | Rol Scrum          |
| -------------- | ------------------ |
| Jorge Huillca  | Scrum Master       |
| Yody Campos    | Backend Developer  |
| Fernando Julca | Backend Developer  |
| Nicolás Meza   | Frontend Developer |

------------------------------------------

## Historias de Usuario

HU1 - Consultar cursos disponibles
  - Como visitante de la plataforma, quiero poder consultar fácilmente todos los cursos disponibles desde una sola página, para revisar las opciones antes de decidirme por uno. Necesito que la información esté organizada y sea clara, para no perder tiempo buscando lo que necesito.

Criterios de aceptación:

- Se muestra un listado con nombre, duración, plataforma y dificultad.

- La página es accesible sin iniciar sesión.

- Los datos se actualizan dinámicamente.

- Los cursos se ordenan por fecha de creación o nombre.
---
HU2 – Registrar un nuevo curso
  - Como usuario de la plataforma, quiero tener una interfaz donde pueda registrar nuevos cursos, para mantener actualizado el catálogo que los usuarios consultan. Necesito que el proceso sea rápido, validado y con confirmación clara al guardar.

Criterios de aceptación:

- El formulario contiene todos los campos requeridos.

- Los campos se validan antes de enviar.

- Muestra un mensaje de éxito si se guarda correctamente.

- Redirige al listado con el curso ya visible.
-------------
HU3 – Modificar un curso existente
  - Como usuario, quiero poder editar la información de un curso ya registrado, para corregir errores o actualizar contenido sin tener que eliminarlo. Espero ver los datos ya cargados y poder modificarlos de forma sencilla.

Criterios de aceptación:
- Al hacer clic en "editar", se muestran los datos actuales.

- El formulario permite modificar y guardar cambios.

- Se valida antes de guardar.

- Muestra un mensaje de confirmación.
----------
HU4 – Eliminar un curso
  - Como usuario, quiero eliminar un curso del sistema cuando ya no esté vigente, para evitar que los usuarios vean información desactualizada o irrelevante. El sistema debe asegurarme que la acción es irreversible.

Criterios de aceptación:

- Se solicita confirmación antes de eliminar.

- El curso desaparece del listado tras la acción.

- Se muestra un mensaje de eliminación exitosa.

- No se afecta la base de datos de otros cursos.
-------
HU5 - Ver los detalles de un curso
  - Como usuario, quiero poder ver más información sobre un curso específico al hacer clic en él, para saber si se ajusta a mis intereses y necesidades antes de contactarme o inscribirme.

Criterios de aceptación:
- El enlace lleva a una página con detalles del curso.

- Se muestran todos los campos (descripción, duración, etc.).

- El diseño es legible y responsivo.

------
