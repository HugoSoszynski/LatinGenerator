import random
from flask import Flask

app = Flask(__name__)


#############################################
#        Sentence Generation Methods        #
#############################################

# Loading the latin wordlist
WORDLIST = []
with open('dict.txt', 'r') as f:
    WORDLIST = f.readlines()
    WORDLIST = list(map(lambda word: word.strip(), WORDLIST))


def generate_sentence_part(min_words: int, max_words: int) -> str:
    words = []
    nb_words = random.randint(min_words, max_words)
    for _ in range(0, nb_words):
        words.append(random.choice(WORDLIST))
    return ' '.join(words)


def generate_sentence() -> str:
    nb_parts = random.choice([1, 1, 2, 2, 2, 2, 3])
    if nb_parts == 1:
        return generate_sentence_part(3, 4)
    else:
        sentence = []
        for _ in range(0, nb_parts):
            sentence.append(generate_sentence_part(2, 3))
        return ', '.join(sentence)


#############################################
#               Flask Routes                #
#############################################

@app.route('/')
def pretty_generator():
    return generate_sentence()

@app.route('/raw')
def raw_generator():
    return generate_sentence()
