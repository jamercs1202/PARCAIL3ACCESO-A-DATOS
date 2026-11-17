# Sistema de Inventario de Zapatos — SQLAlchemy ORM

## 1. Información del proyecto

| Información | Descripción |
|---|---|
| Estudiante | Jamer Carrillo Silva |
| Asignatura | Acceso a Datos |
| Docente | No especificado |
| Fecha | 17 de noviembre de 2026 |
| Lenguaje de programación | Python 3.14.7 |
| ORM utilizado | SQLAlchemy |
| Base de datos | SQLite |

## 2. Descripción del proyecto

### ¿En qué consiste el programa?

El proyecto consiste en implementar la persistencia de datos de una aplicación de inventario para una tienda de zapatos, utilizando Python, SQLAlchemy ORM y SQLite.

El sistema permite administrar los zapatos mediante un menú de consola. Cada zapato contiene un identificador único, modelo, talla y precio.

El archivo `main.py` contiene el menú proporcionado por el profesor y se conserva sin modificaciones. En el archivo `datos.py` se implementaron las funciones necesarias para realizar operaciones sobre la base de datos.

La información se almacena permanentemente en `zapateria.db`, permitiendo conservar los registros después de cerrar el programa.

### ¿Qué funcionalidades tiene?

El sistema permite:

1. **Registrar zapatos:** almacenar nuevos zapatos con su modelo, talla y precio.
2. **Consultar el inventario:** mostrar todos los zapatos registrados.
3. **Buscar zapatos por ID:** localizar un zapato mediante su identificador.
4. **Actualizar precios:** modificar el precio de un zapato existente.
5. **Eliminar zapatos:** retirar registros de la base de datos.
6. **Salir del programa:** finalizar la ejecución.

Estas funcionalidades corresponden a las operaciones CRUD implementadas mediante SQLAlchemy ORM.

## 3. Estructura del proyecto

```text
tienda_zapatos/
├── main.py
├── datos.py
├── requirements.txt
├── README.md
└── evidencias/
    ├── prueba1_registrar.png
    ├── prueba2_listar.png
    ├── prueba3_buscar.png
    ├── prueba4_actualizar.png
    ├── prueba5_eliminar.png
    └── prueba6_persistencia.png
```

### Explicación de los archivos

| Archivo | ¿Cuál es su responsabilidad? |
|---|---|
| `main.py` | Contiene el menú principal, recibe los datos ingresados por el usuario y llama a las funciones de `datos.py`. |
| `datos.py` | Configura SQLAlchemy, define el modelo Zapato, crea la tabla e implementa las cinco operaciones CRUD. |
| `requirements.txt` | Contiene la dependencia SQLAlchemy necesaria para ejecutar el proyecto. |
| `README.md` | Documenta el funcionamiento, la implementación, las pruebas y las respuestas del parcial. |
| `zapateria.db` | Base de datos SQLite que se genera localmente al inicializar el sistema y almacena los registros. |
| `evidencias/` | Carpeta que contiene las capturas de las seis pruebas de funcionamiento. |

El archivo `zapateria.db` se genera automáticamente cuando se ejecuta la inicialización de la base de datos y se establece la conexión necesaria.

## 4. Instalación y ejecución

### Paso 1. Requisitos

Para ejecutar el programa se necesita:

- Python 3.14 o una versión compatible.
- Visual Studio Code o una terminal.
- SQLAlchemy.
- SQLite, disponible mediante Python.
- Una herramienta para instalar las dependencias, como `uv`.

### Paso 2. Instalación de dependencias

Abrir una terminal en la carpeta del proyecto.

Crear un entorno virtual:

```powershell
uv venv --python 3.14
```

Instalar las dependencias:

```powershell
uv pip install -r requirements.txt
```

Durante el desarrollo se utilizó este procedimiento y SQLAlchemy se instaló correctamente.

### Paso 3. Ejecución

Ejecutar el programa con:

```powershell
.\.venv\Scripts\python.exe main.py
```

### Paso 4. Resultado esperado

Al ejecutar correctamente la aplicación aparece el siguiente menú:

```text
===== TIENDA DE ZAPATOS =====
1. Registrar zapato
2. Listar zapatos
3. Buscar zapato por ID
4. Actualizar precio
5. Eliminar zapato
6. Salir
Seleccione una opción:
```

El usuario puede seleccionar cualquiera de las opciones y realizar las operaciones correspondientes.

Al iniciar el programa se crea la tabla `zapatos` si todavía no existe.

## 5. Documentación técnica — Preguntas obligatorias

### Pregunta 1. Modelo y tabla

**¿Qué clase de Python representa la tabla de la base de datos? Explica cómo SQLAlchemy identifica el nombre de la tabla y sus columnas.**

**Respuesta:**

La clase `Zapato`, definida en `datos.py`, representa la tabla de la base de datos.

Esta clase hereda de `Base`, que utiliza `DeclarativeBase` de SQLAlchemy.

SQLAlchemy identifica el nombre de la tabla mediante el atributo `__tablename__`, cuyo valor es `"zapatos"`.

Las columnas se definen utilizando `Mapped` y `mapped_column`, indicando los tipos de datos correspondientes.

El campo `id` es la clave primaria y se genera automáticamente al registrar cada zapato.

Durante las pruebas se registraron Nike Air Max y Adidas Superstar, que recibieron los identificadores 1 y 2.

**Fragmento de código relacionado:**

```python
class Base(DeclarativeBase):
    pass

class Zapato(Base):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(primary_key=True)
    modelo: Mapped[str] = mapped_column(String)
    talla: Mapped[int] = mapped_column()
    precio: Mapped[float] = mapped_column(Float)
```

El modelo permite trabajar con objetos Python que representan registros de la tabla `zapatos`.

### Pregunta 2. Creación de la base de datos

**¿Qué ocurre cuando ejecutas el programa por primera vez? Explica cómo se crea la base de datos `zapateria.db` y la tabla `zapatos`.**

**Respuesta:**

Cuando se ejecuta `main.py`, se llama a la función `datos.inicializar_bd()`.

Esta función utiliza el motor configurado mediante `create_engine()` para establecer la conexión con SQLite.

Si el archivo `zapateria.db` no existe, SQLite lo crea cuando se establece la conexión necesaria.

Después, SQLAlchemy utiliza `Base.metadata.create_all(engine)` para crear la tabla `zapatos` si todavía no existe.

Cuando el programa se ejecuta nuevamente, la tabla existente se conserva y los registros almacenados no se eliminan.

**Fragmento de código relacionado:**

```python
engine = create_engine("sqlite:///zapateria.db")

def inicializar_bd():
    Base.metadata.create_all(engine)
```

En las pruebas se comprobó que la base de datos conservó la información después de cerrar y volver a ejecutar el programa.

### Pregunta 3. Registro de zapatos

**Cuando seleccionas la opción de registrar un zapato, ¿qué recorrido siguen los datos desde el menú hasta quedar almacenados en SQLite? Identifica las funciones utilizadas.**

**Respuesta:**

Cuando seleccioné la opción 1 del menú, el programa solicitó el modelo, la talla y el precio del zapato.

Por ejemplo, registré Nike Air Max, talla 40 y precio de $250.000.

La función `main()` recibió los datos, verificó que fueran válidos y llamó a `datos.crear_zapato(modelo, talla, precio)`.

Esta función creó un objeto de la clase `Zapato`, abrió una sesión de SQLAlchemy y agregó el objeto mediante `sesion.add()`.

Finalmente, `sesion.commit()` confirmó la transacción y guardó el registro en SQLite.

**Fragmento de código relacionado:**

```python
datos.crear_zapato(modelo, talla, precio)
```

Operaciones ORM utilizadas:

```python
zapato = Zapato(modelo=modelo, talla=talla, precio=precio)

with Session(engine) as sesion:
    sesion.add(zapato)
    sesion.commit()
```

El programa mostró el mensaje `Zapato registrado correctamente.`, confirmando que la operación se realizó.

### Pregunta 4. Sesiones y transacciones

**¿Para qué se utiliza una sesión de SQLAlchemy? ¿Qué ocurriría si agregas o modificas un objeto, pero no confirmas la transacción con `commit()`?**

**Respuesta:**

Una sesión de SQLAlchemy permite interactuar con la base de datos mediante objetos Python.

En este programa las sesiones se utilizan para registrar, consultar, actualizar y eliminar zapatos.

Cuando se agrega o modifica un objeto, es necesario confirmar la transacción con `commit()` para guardar permanentemente los cambios.

Si se cierra la sesión sin confirmar una transacción pendiente, los cambios no confirmados se descartan.

**Fragmento de código relacionado:**

```python
with Session(engine) as sesion:
    sesion.add(zapato)
    sesion.commit()
```

Durante el registro de Nike Air Max y Adidas Superstar, las transacciones se confirmaron correctamente, permitiendo consultar los zapatos posteriormente.

### Pregunta 5. Búsqueda por ID

**¿Cómo funciona la búsqueda de zapatos por ID? Explica qué devuelve tu función cuando encuentra el registro y qué devuelve cuando no existe.**

**Respuesta:**

La búsqueda se realiza mediante la función `buscar_zapato(id_zapato)`.

Esta función utiliza una sesión de SQLAlchemy para consultar el registro mediante su clave primaria.

Cuando encuentra el zapato, devuelve un objeto de la clase `Zapato` que contiene su ID, modelo, talla y precio.

Cuando el registro no existe, devuelve `None`.

**Fragmento de código relacionado:**

```python
with Session(engine) as sesion:
    zapato = sesion.get(Zapato, id_zapato)
```

Durante la prueba busqué el ID 1 y el programa mostró:

```text
ID: 1 | Modelo: Nike Air Max | Talla: 40 | Precio: $250000.00
```

Posteriormente, después de eliminar el zapato con ID 2, realicé una búsqueda y el sistema mostró:

```text
Zapato no encontrado.
```

Esto demuestra que la aplicación identifica correctamente los registros existentes e inexistentes.

### Pregunta 6. Actualización de precios

**¿Cómo se actualiza el precio de un zapato mediante el ORM? Explica cómo se obtiene el objeto, cómo se modifica su atributo y cómo se guarda el cambio.**

**Respuesta:**

La actualización se realiza mediante la función `actualizar_precio(id_zapato, nuevo_precio)`.

Primero se abre una sesión y se busca el zapato mediante su identificador.

Si el registro existe, se modifica directamente el atributo `precio` del objeto.

Después se ejecuta `sesion.commit()` para guardar el cambio en SQLite.

**Fragmento de código relacionado:**

```python
with Session(engine) as sesion:
    zapato = sesion.get(Zapato, id_zapato)

    if zapato is None:
        return False

    zapato.precio = nuevo_precio
    sesion.commit()
    return True
```

Durante la prueba actualicé el precio de Nike Air Max, con ID 1, de $250.000 a $280.000.

El programa mostró:

```text
Precio actualizado.
```

Después busqué nuevamente el zapato y comprobé que aparecía con el precio de $280.000.

### Pregunta 7. Eliminación de registros

**¿Qué ocurre cuando eliminas un zapato? Explica cómo compruebas que el registro ya no existe en la base de datos.**

**Respuesta:**

La eliminación se realiza mediante la función `eliminar_zapato(id_zapato)`.

Primero se busca el objeto utilizando su identificador.

Si existe, se utiliza `sesion.delete(zapato)` para marcarlo para eliminación y `sesion.commit()` para confirmar la operación en SQLite.

Si el registro no existe, la función devuelve `False`.

**Fragmento de código relacionado:**

```python
with Session(engine) as sesion:
    zapato = sesion.get(Zapato, id_zapato)

    if zapato is None:
        return False

    sesion.delete(zapato)
    sesion.commit()
    return True
```

Durante la prueba eliminé Adidas Superstar, con ID 2.

El programa mostró:

```text
Zapato eliminado.
```

Después busqué nuevamente el ID 2 y el sistema respondió:

```text
Zapato no encontrado.
```

Así comprobé que el registro había sido eliminado.

### Pregunta 8. Persistencia de datos

**¿Qué sucede con los zapatos registrados cuando cierras y vuelves a ejecutar el programa? Explica por qué permanecen almacenados.**

**Respuesta:**

Los zapatos permanecen almacenados porque SQLite guarda la información en un archivo de base de datos llamado `zapateria.db`.

Los registros no dependen únicamente de la memoria del programa.

Cuando se confirma una operación mediante `commit()`, los cambios quedan guardados en la base de datos.

Durante la prueba seleccioné la opción 6 para cerrar el programa.

Posteriormente ejecuté nuevamente `main.py` y seleccioné la opción 2 para listar los zapatos.

El programa mostró:

```text
ID: 1 | Modelo: Nike Air Max | Talla: 40 | Precio: $280000.00
```

Esto confirmó que Nike Air Max permaneció almacenado con su precio actualizado, incluso después de cerrar y volver a ejecutar la aplicación.

## 6. Pruebas de funcionamiento y evidencias

Se ejecutó el programa desde la terminal de Visual Studio Code y se realizaron las seis pruebas solicitadas.

### Prueba 1. Registrar zapatos

**Acción realizada:** registrar dos zapatos mediante la opción 1 del menú.

**Datos utilizados:**

| Modelo | Talla | Precio |
|---|---|---|
| Nike Air Max | 40 | $250.000 |
| Adidas Superstar | 42 | $320.000 |

**Resultado obtenido:** ambos zapatos se registraron correctamente y el programa mostró el mensaje `Zapato registrado correctamente.` para cada uno.

**Evidencia:**

![Registro de zapatos](evidencias/prueba1_registrar.png)

### Prueba 2. Listar inventario

**Acción realizada:** seleccionar la opción 2 para consultar todos los zapatos.

**Resultado obtenido:**

```text
ID: 1 | Modelo: Nike Air Max | Talla: 40 | Precio: $250000.00
ID: 2 | Modelo: Adidas Superstar | Talla: 42 | Precio: $320000.00
```

Se comprobó que ambos registros estaban almacenados en la base de datos.

**Evidencia:**

![Listado de zapatos](evidencias/prueba2_listar.png)

### Prueba 3. Buscar por ID

**ID utilizado:** 1.

**Resultado obtenido:**

```text
ID: 1 | Modelo: Nike Air Max | Talla: 40 | Precio: $250000.00
```

Se comprobó que el programa encontró correctamente el registro solicitado.

**Evidencia:**

![Búsqueda de zapatos](evidencias/prueba3_buscar.png)

### Prueba 4. Actualizar precio

**Zapato seleccionado:** Nike Air Max, ID 1.

**Precio anterior:** $250.000.

**Precio nuevo:** $280.000.

**Resultado obtenido:** el programa mostró `Precio actualizado.`

Posteriormente se consultó nuevamente el ID 1 y se comprobó que el precio era $280.000.

**Evidencia:**

![Actualización de precio](evidencias/prueba4_actualizar.png)

### Prueba 5. Eliminar zapato

**ID eliminado:** 2.

**Zapato:** Adidas Superstar.

**Resultado obtenido:** el programa mostró `Zapato eliminado.`

Posteriormente se buscó nuevamente el ID 2 y el programa respondió `Zapato no encontrado.`

Esto permitió comprobar la eliminación del registro.

**Evidencia:**

![Eliminación de zapato](evidencias/prueba5_eliminar.png)

### Prueba 6. Comprobar persistencia

**Acción realizada:** cerrar el programa utilizando la opción 6 y ejecutarlo nuevamente.

**Resultado obtenido:** al seleccionar la opción 2, el programa mostró:

```text
ID: 1 | Modelo: Nike Air Max | Talla: 40 | Precio: $280000.00
```

El registro permaneció almacenado y conservó el precio actualizado.

**Evidencia:**

![Persistencia de datos](evidencias/prueba6_persistencia.png)

### Pruebas con registros inexistentes

El sistema contempla las siguientes respuestas cuando se utiliza un ID que no existe:

| Operación | ¿Qué sucede? |
|---|---|
| Buscar ID inexistente | La función devuelve `None` y el menú muestra `Zapato no encontrado.` |
| Actualizar ID inexistente | La función devuelve `False`, muestra `Zapato no encontrado.` y no modifica registros. |
| Eliminar ID inexistente | La función devuelve `False`, muestra `Zapato no encontrado.` y no elimina registros. |

La búsqueda de un ID inexistente se comprobó después de eliminar Adidas Superstar, con ID 2.

Los comportamientos de actualización y eliminación de IDs inexistentes están contemplados en las funciones implementadas.

## 7. Conclusiones

### 1. ¿Qué aprendiste al implementar las operaciones CRUD utilizando SQLAlchemy?

Aprendí a utilizar SQLAlchemy ORM para conectar una aplicación Python con una base de datos SQLite y realizar operaciones CRUD.

También comprendí cómo crear modelos, utilizar sesiones y confirmar transacciones mediante `commit()`.

Las pruebas realizadas permitieron comprobar que los datos pueden registrarse, consultarse, modificarse y eliminarse correctamente.

### 2. ¿Qué diferencia identificaste entre trabajar con objetos Python y escribir sentencias SQL directamente?

La principal diferencia es que SQLAlchemy ORM permite trabajar con clases y objetos Python en lugar de escribir directamente las sentencias SQL para cada operación.

Por ejemplo, para actualizar un precio se obtiene un objeto `Zapato`, se modifica su atributo `precio` y se confirma la transacción.

Esto facilita la organización del código y permite separar las operaciones de persistencia del menú principal.

### 3. ¿Cuál fue la principal dificultad durante el desarrollo y cómo la solucionaste?

La principal dificultad fue configurar correctamente el entorno de Python e instalar SQLAlchemy.

Inicialmente, la terminal de Visual Studio Code no reconocía los comandos `python` y `py`.

Para solucionar el problema utilicé `uv`, creé un entorno virtual con Python 3.14 y ejecuté la instalación de las dependencias mediante:

```powershell
uv venv --python 3.14
uv pip install -r requirements.txt
```

Después seleccioné el intérprete del entorno virtual en Visual Studio Code y ejecuté el programa correctamente.

Finalmente, pude realizar las pruebas CRUD y comprobar que los datos permanecían almacenados después de cerrar y volver a ejecutar el sistema.