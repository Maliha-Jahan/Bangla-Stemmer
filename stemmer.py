from functools import reduce
dictionary_ = list(filter(''.__ne__, open('E:/Thesis/Data/Final/kept.txt',
                                          mode='r', encoding='utf-8').read().split("\n")))
dictionary_en_ = list(filter(''.__ne__, open('E:/Thesis/Data/Final/Dictionary_en.txt',
                                          mode='r', encoding='utf-8').read().split("\n")))
dictionary_en_stemmed_ = list(filter(''.__ne__, open('E:/Thesis/Data/Final/kept_en.txt',
                                          mode='r', encoding='utf-8').read().split("\n")))
suffixes_en = ['ly', 'ness', 'iness', 'ily', 'ish', "n't", "'ve", "'v", "'s", 'ed', "'ll", "'m", "'d",
               'ing', 'ess', 'es', 'er', 'y', 'ism', 's', 'ous', 'ty', 'ity']


def create_dictionary(input_dictionary, div1, div2):
    output_dictionary = [[[] for _ in range(div1)] for _ in range(div2)]
    for word in input_dictionary:
        sum_letters = 0
        for s in range(0, len(word)):
            sum_letters = sum_letters + (ord(word[s]) * (s + 1))
        index1 = (sum_letters * ord(word[len(word) - 1]) * ord(word[0])) % div1
        index2 = (sum_letters * ord(word[len(word) - 1]) * ord(word[0])) % div2
        output_dictionary[index2][index1].append(word)
    return output_dictionary


def create_dict(div1):
    listofwords2 = open('E:/Thesis/Data/Final/suffixes.txt', mode='r', encoding='utf-8').read().split("\n")
    file2 = list(filter(''.__ne__, listofwords2))
    output_dictionary = [[] for _ in range(div1)]
    for word in file2:
        sum_letters = 0
        length = len(word)
        for s in range(0, length):
            sum_letters = sum_letters + (ord(word[s]) * (length - s))
        index1 = (sum_letters * ord(word[length - 1]) * ord(word[0])) % div1
        output_dictionary[index1].append(word)
    return output_dictionary


def hash_find(word, hashed_dictionary, div1, div2):
    sum_letters = 0
    if len(word) == 0:
        return False
    for s in range(0, len(word)):
        sum_letters = sum_letters + (ord(word[s]) * (s + 1))
    index1 = (sum_letters * ord(word[len(word) - 1]) * ord(word[0])) % div1
    index2 = (sum_letters * ord(word[len(word) - 1]) * ord(word[0])) % div2
    return [hashed_dictionary[index2][index1].__contains__(word), index1, index2]


dictionary = create_dictionary(dictionary_, 461, 809)
dictionary_en = create_dictionary(dictionary_en_, 461, 829)
dictionary_en_stemmed = create_dictionary(dictionary_en_stemmed_, 461, 809)
bivokti_dict = create_dict(337)


def stemming2(word):
    length = len(word)
    diff = 0
    if length > 5:
        diff = length - 5
        length = 5
    multiples = [0] * length
    for i in range(0, length):
        multiples[i] = ord(word[i + diff]) * (length - i)
    for s in range(0, length):
        i = length - (s + 1)
        if len(word[:i + diff]) > 0:
            if suffixes_en.__contains__(word[diff + i:]):
                if hash_find(word[:i + diff], dictionary_en_stemmed, 461, 809)[0]:
                    return word[:i + diff]
                new_word = stemming(word[:i + diff])
                if new_word != word[:i + diff]:
                    return new_word
    return word


def stemming(word):
    length = len(word)
    length_word = length
    diff = 0
    if length > 12:
        diff = length - 12
        length = 12
    multiples = [0] * length
    for i in range(0, length):
        multiples[i] = ord(word[i + diff]) * (length - i)
    for s in range(0, length):
        i = length - (s + 1)
        if len(word[:i + diff]) > 0:
            index = (reduce(lambda x, y: x + y, multiples[i:]) * ord(word[length_word - 1]) * ord(word[diff + i])) % 337
            if bivokti_dict[index].__contains__(word[diff + i:]):
                if hash_find(word[:i + diff], dictionary, 461, 809)[0]:
                    return word[:i + diff]
                try:
                    if ord(word[i + diff - 1]) == 2509:
                        word_ = word[:i + diff - 1]
                        if hash_find(word_, dictionary, 461, 809):
                            return word_
                        len_word_ = len(word_)
                        if ord(word_[len_word_ - 2]) == 2439:
                            word_ = word_[:len_word_ - 2] + word_[len_word_ - 1]
                            if hash_find(word_, dictionary, 461, 809):
                                return word_
                    if ord(word[i + diff - 2]) == 2439:
                        word_ = word[:i + diff - 2] + word[i + diff - 1]
                        if hash_find(word_, dictionary, 461, 809):
                            return word_
                    if (ord(word[i + diff - 2]) == 2509) & (word[i + diff - 1] == word[i + diff - 3]):
                        word_ = word[:i + diff - 2]
                        if hash_find(word_, dictionary, 461, 809):
                            return word_
                        len_word_ = len(word_)
                        if ord(word_[len_word_ - 2]) == 2439:
                            word_ = word_[:len_word_ - 2] + word_[len_word_ - 1]
                            if hash_find(word_, dictionary, 461, 809):
                                return word_
                    if word[i + diff - 1] == word[i + diff - 2]:
                        word_ = word[:i + diff - 1]
                        if hash_find(word_, dictionary, 461, 809):
                            return word_
                        len_word_ = len(word_)
                        if ord(word_[len_word_ - 2]) == 2439:
                            word_ = word_[:len_word_ - 2] + word_[len_word_ - 1]
                            if hash_find(word_, dictionary, 461, 809):
                                return word_
                except IndexError:
                    print("oops")
                new_word = stemming(word[:i + diff])
                if new_word != word[:i + diff]:
                    return new_word
    return word

