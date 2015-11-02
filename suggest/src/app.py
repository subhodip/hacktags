#! hacktags-venv/bin/python
from flask import Flask, jsonify
from processors import tagotski

app = Flask(__name__)


# Sample JSON Structure. TODO Should be incoming
questionBlock = [
    {
        'id': 1,
        'question': "",
    },
    {
        'id': 2,
        'question': "",
    },
    {
        'id': 3,
        'question': ""
    }

]


@app.route('/language/api/v0.1/tagoktski', methods=['GET'])
def get_tags():
    question2 = "What personal productivity / time management / motivational tips & tricks do you use"
    tagged = tagotski()
    return jsonify({'tags': tagged.getTags(question2, "english")})


if __name__ == '__main__':
    app.run(debug=True)
