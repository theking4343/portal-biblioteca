from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = "clave123secreta"  # esto deberia ir en una variable de entorno pero para el parcial asi esta bien

# usuarios que existen en el sistema (harcodeados como pidio el profe)
usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}

libros = [
    {"titulo": "Python desde cero", "autor": "Juan Pérez", "disponibles": 4},
    {"titulo": "Desarrollo Web", "autor": "María López", "disponibles": 2},
    {"titulo": "Inteligencia Artificial", "autor": "Pedro García", "disponibles": 0}
]


@app.route("/")
def index():
    # si hay cookie de un login anterior la mostramos
    ultimo_usuario = request.cookies.get("ultimo_usuario")
    return render_template("index.html", ultimo_usuario=ultimo_usuario)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        if usuario in usuarios and usuarios[usuario] == password:
            session["usuario"] = usuario

            resp = make_response(redirect(url_for("libros_view", bienvenida=1)))
            resp.set_cookie("ultimo_usuario", usuario, max_age=2592000)  # 30 dias
            return resp

        error = "Usuario o contraseña incorrectos."

    return render_template("login.html", error=error)


@app.route("/libros")
def libros_view():
    usuario = session.get("usuario")
    bienvenida = request.args.get("bienvenida")
    return render_template("libros.html", libros=libros, usuario=usuario, bienvenida=bienvenida)


@app.route("/perfil")
def perfil():
    # si no inicio sesion, para /login nomas
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("perfil.html", usuario=session["usuario"])


@app.route("/eliminar-cookie")
def eliminar_cookie():
    resp = make_response(redirect(url_for("index")))
    resp.delete_cookie("ultimo_usuario")
    return resp


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index", logout=1))


if __name__ == "__main__":
    app.run(debug=True)
