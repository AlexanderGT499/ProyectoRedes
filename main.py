from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def cargar_html():
    # Renderiza el archivo HTML desde la carpeta templates
    return render_template('sitios/index.html')

if __name__ == "__main__":
    app.run(debug=True)
