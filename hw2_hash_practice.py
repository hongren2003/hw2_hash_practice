def main():
    # main function
    f = open('./hw2_data.txt', 'r') # file object 'hw2_data.txt' (read-only mode)
    hash(f) # run the hash function
    f.close # close the file object f

def hash(file):
    # function to hash and print the result
    dictionary = {} # hash table
    word = file.readline() # var to store the first line in the file
    word = word.rstrip('\n') # remove the new line (\n) escape character
    while word:
        if word in dictionary:
            # value (frequency) + 1
            dictionary[word] = dictionary[word] + 1
        else:
            # add the word into the dictionary and set it value = 1)
            dictionary[word] = 1
        word = file.readline() # read the next line
        word = word.rstrip('\n')
    print('All words in the file and their frequency:')
    for i in dictionary:
        # print all words in the file and their frequency
        print(i, dictionary[i], sep = '\t')

if __name__ == '__main__':
    # entry point
    main()