# put your code here.
my_file = open('test.txt')

counting_words = {}

def count():
    for line in my_file:
        line = line.strip().split()
        for word in line:
            counting_words[word] = counting_words.get(word,0) + 1
    print counting_words

    my_file.close()

count()