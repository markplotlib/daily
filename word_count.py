# https://www.pythonmorsels.com/exercises/9af6665915964ee7ba19fe3d762d9ca8/submit/1/#problem
#
# I want you to write a function that accepts a string and returns a mapping
# (a dictionary or dictionary-like structure) that has words as the keys
# and the number of times each word was seen as the values.

def count_words(s):
    wordlist = s.lower().split()
    keyset = set(wordlist)
    counts = {}
    for key in keyset:
        counts[key] = 0
    for word in wordlist:
        counts[word] += 1
    return counts

if __name__ == '__main__':
    print(count_words("Oh what a day what a lovely day"))
    # {'Oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

    print(count_words("don't stop believing"))
    # {"don't": 1, 'stop': 1, 'believing': 1}
