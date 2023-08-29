# Practica_IEB

Configuración del Backend

# Requisitos
Python 3.x
Django 4.x
Virtualenv (opcional pero recomendado)
Pasos

1. Clona este repositorio en tu máquina local.

2. Crea un entorno virtual (opcional pero recomendado):

   python -m venv venv

3. Activa el entorno virtual:

   -> Windows: venv\Scripts\activate
   -> macOS y Linux: source venv/bin/activate

4. Instala las dependencias del proyecto:

   pip install -r requirements.txt

5. Realiza las migraciones de la base de datos:

   Gestor: Postgres
   Name DB: Practica_IEB

6. Inicia el servidor de desarrollo:

   python manage.py runserver
   
El backend estará disponible en http://127.0.0.1:8000/.

Configuración del Frontend
Pasos

  1. Abre el archivo detalle_producto.html en la carpeta templates y actualiza las URLs en las solicitudes fetch para que apunten a las rutas correctas del backend.

  2. Abre el archivo mostrar_informacion.html y realiza el mismo paso que en el punto anterior.

  3. Abre el archivo crear_producto.html y realiza el mismo paso que en los puntos anteriores.

  4. Abre detalle_producto.html y mostrar_informacion.html y verifica que las etiquetas <select> y los botones tengan los IDs y clases correctos para que el JavaScript funcione correctamente.
