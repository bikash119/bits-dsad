#!/usr/bin/env python
# coding: utf-8

# In[56]:


import os.path
import string

# Node Class with constructor and is_wordPalindrome methods
# is_wordPalindrome method takes each word in queue, converts to String and returns true/false if its palindrome
class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def is_wordPalindrome(word): #aaaaa
        if(word.data is None):
            print("Node in LL is empty")
            return False 
        else:
            lower_word = word.data.lower()
            # create Queue instance
            charQueueLL_Q2 = QueueLinkedList() 
            charQueueLL_Q3 = QueueLinkedList() 
            #add characters of word to the queue dataQueueLL_Q2
            [charQueueLL_Q2.queueEnq(ch) for ch in lower_word ]
            
            #add characters of reversed word to the queue dataQueueLL_Q3
            reversed_word = word.data[::-1]
            [charQueueLL_Q3.queueEnq(ch) for ch in reversed_word ]
            char_queue_size = charQueueLL_Q2.getSize()
            while (char_queue_size > 1):
                if (charQueueLL_Q2.queueDeq() != charQueueLL_Q3.queueDeq()):
                    return False
                char_queue_size = char_queue_size -1
            return True
        
# Class for Queue single LinkedList object 

class QueueLinkedList(object):
    
    # constructor for first & last nodes - head & tail
    def __init__(self):
        self.head = None
        self.tail = None
        
    #checkPalindrome method checks if each word in queue is palindrome or not. If yes, inserts at rear end of queue
    def checkPalindrome(self): 
        cur_node = self.head
        queueSize=self.getSize()

        if(self.head is None):
            print("Node is empty")
        else:
             while (queueSize>=1):
                if(cur_node.is_wordPalindrome()):
                    queueSize=queueSize-1
                    if(self.queueDeq() is not None):
                        self.queueEnq1(cur_node.data)
                        cur_node = cur_node.next                    
                else:
                    if(self.queueDeq() is not None):
                        queueSize=queueSize-1
                        cur_node = cur_node.next

                
    
    # size of the queue as it traverses the queue-O(n)                      
    def getSize(self):
        count=0
        cur_node=self.head
        while cur_node:
            count=count+1
            cur_node = cur_node.next
        return count
    
    def list_reverse(self):
        prev_node = None 
        cur_node = self.head
        next_node=self.head
        while cur_node:
            next_node = next_node.next
            cur_node.next = prev_node
            prev_node=cur_node
            cur_node=next_node
        self.head = prev_node 
    
    # Converts queue to String for output
    def queueToString(self):
        cur_node = self.head
        LLString=""
        if(self.head is None and self.tail is None):
            print("Node is empty")
        while cur_node:
            LLString=LLString+cur_node.data+" "
            cur_node = cur_node.next
        return LLString
    
    # Appends each word to the rear end of the linked list queue
    def queueEnq(self, data):
        new_node = LLNode(data)
        # checks if any nodes exists and if none assign new node to head node
        if(self.head is None and self.tail is None):
            self.head = new_node
            self.tail = new_node
        else:
            print(self.tail.data)
            self.tail.next=new_node
            self.tail=new_node
        return self
    
    def queueEnq1(self, data):
        new_node = LLNode(data)
        # checks if any nodes exists and if none assign new node to head node
        if(self.head is None and self.tail is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        return self
    
    # Prints the queue linked list
    def printQueueList(self):
        cur_node = self.head
        if(self.head is None and self.tail is None):
            print("Node is empty")
        while cur_node:
            cur_node = cur_node.next
    
    # Removes the word from the front end of the queue      
    def queueDeq(self):
        cur_node = self.head
        if(self.head is None and self.tail is None):
            print("Node is empty, Nothing can be deleted")
            return None
        else:
            self.head = cur_node.next
            return cur_node
        
    
    # load input data from File
    def loadDataFromFile(self,fname):
        if(os.path.exists(fname)):
            with open(fname,"r") as rf:
                inDataString=""
                for line in rf:
                    inDataString=inDataString+line
                rf.close()
                return inDataString
        else:
            return None
    
    # Process input string with punctuations and split using space delimiter   
    def processInputDataString(self,inDataString):
        dataStringList=inDataString.split(" ")
        table=str.maketrans("","",string.punctuation)
        stripStringList= [w.translate(table) for w in dataStringList]
        return stripStringList
    
    # write palindrome queue data to file
    def writeDataToFile(self,fname,data):
        with open(fname,"w") as wf: 
            if(len(data)>0):
                wf.write(data)
                wf.close()
                return True
            else: 
                return False
                wf.close()
        
# Main class of method invocations
class MainFunction():
    
    try: 
        if __name__ == "__main__":

            # create Queue instance
            dataQueueLL_Q1 = QueueLinkedList()

            # Read data from Input File
            fname="inputPS15.txt"
            inDataString=dataQueueLL_Q1.loadDataFromFile(fname)

            if(inDataString is not None):
                dataStringList=dataQueueLL_Q1.processInputDataString(inDataString) 
                print(dataStringList)
                # Append input string to queue
                for eachWord in dataStringList:
                    dataQueueLL_Q1.queueEnq(eachWord)
                
                # check if queue words are palindrome
                dataQueueLL_Q1.checkPalindrome()

                # convert palindrome queue words to data string
                outPalindromeString=dataQueueLL_Q1.queueToString()                

                # Write Palindrome queue to File
                wfname="outputPS15.txt"
                writeSuccess=dataQueueLL_Q1.writeDataToFile(wfname,outPalindromeString)
                if(writeSuccess):
                    print("Palindrome data Successfully Written To File")
                else:
                    print("Palindrome data is not written, No Palindrome data or error occurred")

            else:
                print("No Data Exists in the file, Place the data file and re-run the program") 

    except: #catch *all* exceptions
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e )


# In[ ]:





# In[ ]:





# In[ ]:




