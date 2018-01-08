# put your code here.
def counter(input_file):
    '''Opens a file & counts the number of times a word appears'''
    with open(input_file) as f:
        word_count = {}

        for line in f:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        # f.close()

    for word, count in word_count.iteritems():
        print word, count
    # for item in word_count.items():
    #     print item[0], item[1]

input_file = "twain.txt"
counter(input_file)
