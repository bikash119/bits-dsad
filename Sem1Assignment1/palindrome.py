# -*- coding: utf-8 -*-
"""
Spyder Editor

"""


"""
    Create a Queue using doubly linked list
"""

import re

class Node:
    
# initialize the node object
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    
# intialize the head
    def __init__(self):
        self.head = None
        self.last = None
    
    def enqueue(self,data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head.prev = None
            self.head = self.head.next
            return temp
    
    def printQueue(self,tag):
        print("\n")
        print(f'{tag} Queue elements :')
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next

def recursive_palindrome_check(word):
    if len(word) == 1:
        return True
    first_letter = word[0]
    last_letter = word[len(word) -1]
    if first_letter != last_letter:
        return False
    else:
        new_word = word[1:-1]
        return recursive_palindrome_check(new_word)

def is_palindrome(word):
    if len(word) == 1:
        return True
    else:
        return recursive_palindrome_check(word)

input_queue = Queue()
output_queue = Queue()
with open('inputPS15.txt', 'r') as reader:
    for line in reader.readlines():
        # remove punctuation
        cleaned_line = re.sub(r'[^\w\s]', '', line)
        for word in cleaned_line.split():
            input_queue.enqueue(word)

input_queue.printQueue("input")
# iterate over input queue
curr_word = input_queue.dequeue()
while curr_word is not None:
    if is_palindrome(curr_word):
        output_queue.enqueue(curr_word)
    curr_word = input_queue.dequeue()

output_queue.printQueue("output")

input_queue = Queue()
#populate input queue
palindrome = output_queue.dequeue()
while palindrome is not None:
    input_queue.enqueue(palindrome)
    palindrome = output_queue.dequeue()

print("input queue after population")
input_queue.printQueue("input")







"""
    TODO : check for empty string
"""
#for line in all_lines:
#    for word in line.split():
#        words.append(word)
#
#word_size = len(words)
## Create input Queue
#
#
        
#        
#    
#for index in range(word_size):
#    word = words.popleft()
#
#    if is_palindrome(word):
#        words.append(word)
#        
##Dump the output of queue to file
#output_file = open('outputPS15.txt','a')
#for index in range(len(words)):
#    pali_word =  words.popleft()
#    output_file.write(pali_word)
#    output_file.write(" ")
#output_file.close()



    







    
