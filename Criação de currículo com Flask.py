from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def decoratorex():
    return ''' <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - [Seu Nome]</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .cv-container {
            background-color: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        header {
            text-align: center;
            border-bottom: 2px solid #3498db;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }
        h1 { margin: 0; color: #2c3e50; }
        .contact-info { color: #7f8c8d; font-size: 0.9em; }
        h2 { color: #3498db; border-bottom: 1px solid #eee; padding-bottom: 10px; }
        .section { margin-bottom: 25px; }
        .item { margin-bottom: 15px; }
        .item-title { font-weight: bold; color: #2c3e50; }
        .item-subtitle { font-style: italic; color: #7f8c8d; }
        .date { float: right; color: #95a5a6; font-size: 0.9em; }
        ul { margin-top: 5px; }
        
        /* Estilo para idiomas */
        .language-skills {
            display: flex;
            gap: 20px;
        }
        .lang { flex: 1; }
        .bar {
            background-color: #ddd;
            border-radius: 10px;
            height: 10px;
            margin-top: 5px;
        }
        .fill {
            background-color: #3498db;
            height: 10px;
            border-radius: 10px;
        }
    </style>
</head>
<body>

<div class="cv-container">
    <header>
        <h1>[SEU NOME COMPLETO]</h1>
        <p class="contact-info">
            [Cidade, Estado] | [Seu Telefone] | [Seu E-mail]
        </p>
    </header>

    <section class="section">
        <h2>Experiência Profissional</h2>
        
        <div class="item">
            <span class="date">[Mês/Ano] - [Atual]</span>
            <div class="item-title">[Nome da Empresa] - [Seu Cargo]</div>
            <ul>
                <li>[Realização ou responsabilidade 1]</li>
                <li>[Realização ou responsabilidade 2]</li>
            </ul>
        </div>

        <div class="item">
            <span class="date">[Mês/Ano] - [Mês/Ano]</span>
            <div class="item-title">[Empresa Anterior] - [Seu Cargo]</div>
            <ul>
                <li>[Realização ou responsabilidade 1]</li>
            </ul>
        </div>
    </section>

    <section class="section">
        <h2>Formação Acadêmica</h2>
        <div class="item">
            <span class="date">[Ano de Conclusão]</span>
            <div class="item-title">[Nome do Curso/Graduação]</div>
            <div class="item-subtitle">[Nome da Instituição/Escola]</div>
        </div>
    </section>

    <section class="section">
        <h2>Cursos e Certificações</h2>
        <ul>
            <li>[Nome do Curso] - [Instituição] ([Ano])</li>
            <li>[Nome do Curso] - [Instituição] ([Ano])</li>
        </ul>
    </section>

    <section class="section">
        <h2>Idiomas</h2>
        <div class="language-skills">
            <div class="lang">
                <strong>Inglês:</strong> [Nível: ex. Fluente]
                <div class="bar"><div class="fill" style="width: 80%;"></div></div>
            </div>
            <div class="lang">
                <strong>Espanhol:</strong> [Nível: ex. Intermediário]
                <div class="bar"><div class="fill" style="width: 50%;"></div></div>
            </div>
        </div>
    </section>
</div>

</body>
</html>

  '''

if __name__ == '__main__':
    app.run(debug=True)