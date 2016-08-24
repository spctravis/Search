import string
from collections import Counter
file_name = open("test.txt", "r")

line = file_name.read()

print(line)

search = input('What word you looking for? ')
words = line.lower().split()

exclude = set(string.punctuation)
my_counter = {}
word_list = []


for lines in words:
    s = ''.join(ch for ch in lines if ch not in exclude)
    if search in s:
        word_list.append(search)
        word = s.strip()

        if word not in my_counter:
            my_counter[word] = 1
        else:
            my_counter[word] += 1
        print(s, "is found: ", + my_counter[word], "times")

count = Counter(word_list)
print(count)

file_name.close()

