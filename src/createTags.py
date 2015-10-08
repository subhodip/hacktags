#! hacktags-venv/bin/python
## Main code for Natural Language Pre Processing.
import nltk
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet



## Sample question Block, replace with a stream
question1 = "How much does physical appearance matter for becoming a successful entrepreneur"
question2 = "What personal productivity / time management / motivational tips & tricks do you use"
question3 = "How accurate were Carly Fiorina's claims about HP during the September 2015 Republican debate"
trainQuestion = ""
lang = "english"

def removeStopWordsByLang(lang):
    return set(stopwords.words(lang))

def tags(text):
    return word_tokenize(text)

def filterSentences(text, lang):
    filteredSentence = []
    words = tags(text)
    stop_words = removeStopWordsByLang(lang)
    for word in words:
        if word not in stop_words:
            filteredSentence.append(word)
    return filteredSentence
def sentenceTagging(text, trainingText):
    csTokenizer = PunktSentenceTokenizer(trainingText)
    tokenized = csTokenizer.tokenize(text)
    taggedSentence = []
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            taggedSentence.append(tagged)
            #chinkingWords(tagged).draw()
            namedEntityRecog(tagged)
    except Exception as e:
        print(str(e))

    return taggedSentence

def stemmingWords(wordList):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in wordList]

def chunkingWords(text):
    chunkGram = r"""Chunk:{<RB.?>*<VB.?>*<NNP>+<NN>} """
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(text)
    return chunked

def chinkingWords(text, regex):
    chunkGram = r"""Chunk: {<.*>+}
    }<VB.?| IN| DT | TO>+{ """
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(text)
    return chunked

def namedEntityRecog(text):
    namedEnt = nltk.ne_chunk(text)
    namedEnt.draw()
    return namedEnt

def lemmatizer(word, flag):
    lemmatized = WordNetLemmatizer()
    return lemmatized.lemmatize(word, flag)

def wordnetFunction(word):
    synWordList = []
    WordDefination = []
    #word
    syns = wordnet.synsets(word)
    for i in syns:
        synWordList.append(i.name())
    return synWordList
#print stemmingWords(filterSentences(question3, lang))
print sentenceTagging(question3, question1)
#print lemmatizer("better", "a")
#print wordnetFunction("question")