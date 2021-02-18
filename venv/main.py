from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer

crimefile = open("passio.txt", 'r')
lemmatized = open("lemmatized.txt", 'w')

tokens = []
for line in crimefile:
    tokens= line.split()
lemmatizer = BackoffLatinLemmatizer()
out = lemmatizer.lemmatize(tokens)

for word in out:
    string = word[1] + "\n"
    lemmatized.write(string)

