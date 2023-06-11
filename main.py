from flask import Flask
import os

app = Flask(__name__)

def find_most_common_word(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_common_word = max(word_count, key=word_count.get)
        return most_common_word

@app.route('/find_most_common_word/<path:file_path>')
def get_most_common_word(file_path):
    if os.path.isfile(file_path):
        most_common_word = find_most_common_word(file_path)
        return f'The most common word in {file_path} is "{most_common_word}"'
    else:
        return f'File {file_path} not found'

if __name__ == '__main__':
    app.run()