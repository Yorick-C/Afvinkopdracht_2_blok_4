from flask import Flask, render_template, request
from converter_code import code

app = Flask(__name__)


@app.route('/')
def sequentie_app():
    sequentie = request.args.get("sequentie", "")
    proteinseq = protein_seq(sequentie)
    return render_template("html_afvink_2.html", sequentie=sequentie
                           , code=code, proteinseq=proteinseq)


def protein_seq(sequentie):
    proteinseq = ""
    if len(sequentie) % 3 == 0:
        for i in range(0, len(sequentie), 3):
            x = sequentie[i:i + 3]
            proteinseq += code[x]
    return proteinseq


if __name__ == '__main__':
    app.run()
