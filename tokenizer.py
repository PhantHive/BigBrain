import json
from src.stemming import IrisStemmer
from src.lemmer import IrisLemmer
import os.path
from src.one_hot import OneHot

class TOKENIZE:
    def __init__(self, text):
        self.text = text
        self.all_sentences = []
        self.sentence = ""
        self.new_text = ""
        self.all_words = []
        self.tokenize_matrix = []
        # self.stemmer = IrisStemmer()

        stopwords = open(os.path.abspath("assets/stopwords/stop_words_french.json"), "r")
        self.stopwords = json.load(stopwords)
        self.text_to_sentences()

    def text_to_sentences(self):
        end_sentence = ["!", "?", ".", ":", ";"]

        for let in self.text:
            if let in end_sentence:
                self.sentence = (self.text.split(let, 1)[0]).split()

                for word in self.sentence:
                    if "," in word and word.index(",") > 0:
                        z = self.sentence.index(word)
                        self.sentence[z] = "".join(word.split((",", 1)[0]))
                    if word == "":
                        self.sentence.remove(word)
                for word in self.sentence:
                    for i in word:
                        if i.isupper() and word.index(i) > 0:
                            z = self.sentence.index(word)
                            self.sentence[z] = word.split(i, 1)[0]
                            self.sentence.insert(
                                z + 1,
                                i + word.split(i, )[1],
                            )
                for word in self.sentence:
                    if "'" in word and word.index("'") > 0:
                        z = self.sentence.index(word)
                        self.sentence[z] = word.split("'", 1)[0]
                        self.sentence.insert(
                            z + 1,
                            word.split("'", )[1],
                        )
                    if word == "":
                        self.sentence.remove(word)

                        self.sentence.insert(
                            z + 1,
                            i + word.split(i, )[1],
                        )

                self.new_text = self.text.split(let, 1)[1]
                self.all_sentences.append(self.sentence)
                self.text = self.new_text

        self.tokenize()

    def tokenize(self):



        for word in self.all_sentences:
            if word not in self.stopwords:
                self.all_words += word

        self.all_words = [
            word for word in self.all_words
            if word.lower() not in self.stopwords
        ]
        self.all_words.sort()

        lemmer = IrisLemmer() # Lemmatize all words
        self.all_words = lemmer.lemmer(self.all_words)

        oh_encode = OneHot(self.all_sentences, self.all_words)
        self.tokenize_matrix = oh_encode.encode()


    def show_sentences(self):
        return self.all_sentences, self.tokenize_matrix, self.all_words


# tries ===============================


'''text = ("En mon c??ur n'est point escrite"
         "La rose ny autre fleur,"
         "C'est toy, blanche Marguerite,"
         "Par qui j'ay cette couleur."
         "N'es-tu celle dont les yeux"
         "Ont surpris"
         "Par un regard gracieux"
         "Mes esprits ?"
         "Puis que ta s??ur de haut pris,"
         "Ta s??ur, pucelle d'??lite,"
         "N'est cause de ma douleur,"
         "C'est donc par toy, Marguerite"
         "Que j'ay pris ceste couleur."
         "Ma couleur palle nasquit,"
         "Quand mon c??ur"
         "Pour maistresse te requit ;"
         "Mais rigueur"
         "D'une amoureuse langueur"
         "Soudain paya mon m??rite,"
         "Me donnant ceste p??leur"
         "Pour t'aimer trop, Marguerite,"
         "Et ta vermeille couleur."
         "Quel charme pourroit casser"
         "Mon ennuy"
         "Et ma couleur effacer"
         "Avec luy ?"
         "De l'amour que tant je suy"
         "La jouissance subite"
         "Seule osteroit le malheur"
         "Que me donna Marguerite,"
         "Par qui j'ay cette couleur.")

text = "Avec l'exemple des pi??ces de Corneille, Moli??re et Racine, on montre quelques-uns des nombreux " \
        "usages possibles des bases de donn??es textuelles normalis??es et lemmatis??es. Elles sont d'une " \
        "consultation ais??e. Elles fournissent de nombreux renseignements sur le vocabulaire, le style, le sens " \
        "des mots... Pour cela, il faut r??duire les graphies multiples et rattacher chaque mot ?? son entr??e de " \
        "dictionnaire."

test = TOKENIZE(text)
res, res2, res3 = test.show_sentences()



# stemmer = IrisStemmer()
# res3 = stemmer.stemmer(res3)



# lemmer = IrisLemmer()
# res3 = lemmer.lemmer(res3)


print(res3)
for lst in res2:
    print(lst)
print(res)'''
