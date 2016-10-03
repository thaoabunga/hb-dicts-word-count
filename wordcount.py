# put your code here.

def tokenize(file_path):
    """return a list of words from the file"""
    tokens = []
    my_file = open(file_path)
    for line in my_file:
        line = line.strip().split()
        tokens.extend(line)
    print tokens

tokenize('test.txt')

def count():

    counting_words = {}

    for word, value in counting_words.items():
            counting_words[word] = counting_words.get(word,0) + 1
            
    print counting_words

    # print 'word = %r, value = %r' % (word, value)

# def text(word):
#     # return counting_words.get(word, 0)
#     print counting_words

# count()

# # #1. function1: open the my_file
# # #2 function2: create dictionary
# # #3 function3: print the keys and values of the dictionary

# my_file = open('test.txt')

# counting_words = {}

# def count():
#     for line in my_file:
#         line = line.strip().split()
#         for word in line:
#             counting_words[word] = counting_words.get(word,0) + 1
#     print counting_words

#     my_file.close()

# count()