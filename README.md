# hw2_hash_practice

Repository link: https://github.com/hongren2003/hw2_hash_practice

Hong-Ren, Huang (B507110048)

School of Public Health, Taipei Medical University

XB500070: Fundamental Data Structure & Algorithm

March 24, 2023

# Description

A tool based on python to calculate frequency of each word in a specified file.

# Method

Use hash (dictionary) structure to store each duplicate word (key) and its occurrence (value).

Critical code block:

```py
while word:
    if word in dictionary:
        # value (frequency) + 1
        dictionary[word] = dictionary[word] + 1
    else:
        # add the (new) word into the dictionary and set it value to 1)
        dictionary[word] = 1
```

Please refer to the source code file for more details.

# Results

(Input: given "hw2_data.txt")

```
All words in the file and their freqencies:
Cheese  234
Pizza   83
Coke    145
Steak   46
Burger  196
Fries   76
Rib     33
Taco    57
Pho     19
Potato  3
```