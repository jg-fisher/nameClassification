#import keras
#from keras.layers import Dense
#from keras.models import Sequential

from sklearn.preprocessing import OneHotEncoder
#from sklearn.utils import shuffle

# get the length of the longest name
def characterize():
        with open('data.csv', 'r') as f:
            longest = 0
            chars = ''
            labels = []
            for line in f:
                split = (line.rstrip()).split(',')
                labels.append(split[1])
                name = split[0]
                chars += name
                if len(name) > longest:
                    longest = len(name)

            char_set = set([c for c in chars if c is not " "])
            labels = set(labels)

            return char_set, labels, longest


if __name__ == '__main__':

    char_set, labels, _ = characterize()

    # dictionaries for conversions
    char_to_int = {c:i for i, c in enumerate(sorted(char_set))}
    label_to_class = {l:c for c, l in enumerate(labels)}
    print(label_to_class)

    # network input and output
    X = []
    Y = []

    with open('data.csv', 'r') as f:
        for line in f:

            # converting chars in words to integers
            split = (line.rstrip()).split(',')
            name_chars = [c for c in split[0] if c is not ' ']
            xi = [char_to_int[c] for c in name_chars]
            yi = label_to_class[split[1]]

            X.append(xi)
            Y.append(yi)

    # one hot encoding names
    ohe = [[0] * len(char_set) for xi in range(len(X))]
    for index, word in enumerate(X):
        for int_value in word:
            ohe[index][int_value] = 1

    
