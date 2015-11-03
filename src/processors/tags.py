#! hacktags-venv/bin/python
## This code takes in a sentence or a paragraph and then breaks out into words of choice(nouns, verbs, named entities
# etc). It then creates all the synonyms and create a tag cloud with those tags.
# imports start
import nltk
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
# import ends

class tagotski(object):
    ##Example text, move this to tests later
    ## Sample question Block, replace with a stream
    #question1 = "How much does physical appearance matter for becoming a successful entrepreneur"
    #question2 = "What personal productivity / time management / motivational tips & tricks do you use"
    #question3 = "How accurate were Carly Fiorina's claims about HP during the September 2015 Republican debate"
    #trainQuestion = ""
    #lang = "english"
    ##Example text ends
    
    # Parse the sentence and tokenize them with part of speech tag
    def getTags(self, text, lang):
        filteredSentence = []
        stoppedWords = set(stopwords.words(lang))
        words = word_tokenize(text)
        for word in words:
            if word not in stoppedWords:
                filteredSentence.append(word)

        return nltk.pos_tag(filteredSentence)


    # use wordnet to find synonyms to words
    def findSyns(self, word):
        return None


    # use wordnet to find defination of words
    def findDef(self, word):
        return None


    # use wordnet to find similar to word
    def findSim(self, word):
        return None


    # use wordnet to find antonym to words
    def findAnty(self, word):
        return None
