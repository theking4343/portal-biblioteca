# Portal de Biblioteca - TEM-742

Parcial de Tecnologías Emergentes II. Es una app en Flask que simula el acceso
de usuarios a una biblioteca (login, sesiones, cookies y templates con Jinja2).

## Usuarios para probar

- carlos / 1111
- laura / 2222
- diego / 3333

## Cómo correrlo

```
python -m venv venv
venv\Scripts\activate      (en windows)
source venv/bin/activate   (en mac/linux)

pip install -r requirements.txt
python app.py
```

Después entrar a http://127.0.0.1:5000/

## Qué hace cada cosa

- `/` - inicio, muestra si hay un usuario guardado en cookie
- `/login` - formulario para iniciar sesión
- `/libros` - lista de libros (se pinta con un for de Jinja2)
- `/perfil` - solo se puede ver si iniciaste sesión, si no te manda a /login
- `/logout` - cierra la sesión y vuelve al inicio

## Notas

- La cookie `ultimo_usuario` se guarda al hacer login y dura 30 días, se puede borrar desde el inicio.
- venv no se sube al repo (está en .gitignore).
