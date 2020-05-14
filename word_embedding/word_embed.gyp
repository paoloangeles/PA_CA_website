### word embedding model ###

import nltk
nltk.download('punkt')

class word_embed():

    def __init__(self, file_name):
        self.text_file_name = file_name
        self.convert_input_textfile()

    def convert_input_textfile(self):
        self.test_file = open(self.text_file_name, 'r')
        self.test_text = self.test_file.read()

    def tokenise_textfile(self):
        return nltk.word_tokenize(self.test_text)

    def close_textfile(self):
        self.test_file.close()


test = word_embed("test.txt")
print(test.tokenise_textfile())



