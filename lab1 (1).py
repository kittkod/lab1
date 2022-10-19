#edit code to get rid of lists and do EC work. 
class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the
        class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.
        
        Parameters
        ----------
        data : None type
        
        Result
        ------
        change of data.
        '''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.
        
        Parameters
        ----------
        next_node : type Node 
        
        Result
        ------
        new next node is set.
        '''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.''' 
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node


class Queue(object):
    """A class to reprent a queue with a singly-linked list.
    
    ...

    Attributes
    ----------
    head : An object of type Node
        Used to track where the beginning of the queue is
    tail : An object of type Node
        Used to track where the end of the queue is

    Methods
    -------
    __str__() :
        Return a formatted string for printing the queue.
    enqueue(newData) :
        Create a new node with newData and add it to the queue. 
    dequeue() :
        Return the head of the queue and update the head. 
    isEmpty() : 
        Check if queue is empty. 

    """
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        # start at the head node and loop to each node following and 
        # print it
        reslis = []
        currentnode = self.__head
        while currentnode != None:
            reslis.append(currentnode.getData())
            currentnode = currentnode.getNext()
        return str(reslis)        

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next 
        node is null and update head and tail.

        ...

        Parameters
        ----------
        newData: an int, float or str
            Data that will be in the new node that will append to the 
            queue
        
        '''
        # creating  a node whos data equals newData
        new = Node(newData, None)
        # setting the head to equal the new node if its the first 
        # item in the queue
        if self.__head == None:
            self.__head = new
            self.__tail = self.__head
        else:
            self.__tail.setNext(new)
            self.__tail = new

    def dequeue(self):
        '''Return the head of the Queue and update head.
        
        Exceptions
        ----------
        Runtime error: raised when dequeuing from an empty queue
        '''
        # checking if the queue is empty
        if self.__head == None:
            raise RuntimeError("Dequeuing from an empty Queue.")
        # creating a var for head and shifting head
        ret = self.__head.getData()
        self.__head = self.__head.getNext()
        return ret

    def isEmpty(self):
        '''Check if the Queue is empty.check if queue is empty. '''
        return self.__head == None


class Stack(object):
    """A class to represent a stack.

    ...

    Attributes
    ----------
    top : an object of type Node
        used to show where the top of the Stack is

    Methods
    -------
    __str__():
        Gathers each Node's data and return a formatted string 
        for printing stack
    push(newData):
        Pushes a new node onto the stack
    pop():
        Pops the top item (self.__top) from the stack and updates 
        top

    """
    def __init__(self):
        '''Initializing stack top as empty.'''
        self.__top = None

    def __str__(self):
        '''Looping through your stack and print each Node's data.'''
        reslis = []
        curr = self.__top
        while curr != None:
            reslis.append(curr.getData())
            curr = curr.getNext()
        return str(reslis)        

    def push(self, newData):
        '''Create a node whose data is newData and next node is 
        top and push this new node onto the stack.

        ...

        Parameters
        ----------
        newData: int, str or float
            Data that you will push to the stack to become the 
            new top
            
        '''
        new1 = Node(newData, self.__top)
        self.__top = new1

    def pop(self):
        ''' Return the Node that currently represents the top of 
        the stack and update stack.
        
        Exceptions
        ----------
        Runtime Error : raised when popping from an empty stack.
        '''
        if self.__top == None:
            return RuntimeError("Popping from an empty stack.")
        temp = self.__top.getData()
        self.__top = self.__top.getNext()
        return temp

    def isEmpty(self):
        '''Check if the Stack is empty. '''
        return self.__top == None


def isPalindrome(s):
    '''Using Queue and Stack class to test weather an input is a 
    palindrome.'''
    myStack = Stack()
    myQueue = Queue()
    # making the string lowercase without spaces
    s = s.lower().replace(' ', '')

    # pushing and enqueuing the letters of s onto a queue and stack
    for i in range(len(s)): #from 0 to len(s)-1
        myStack.push(s[i])
        myQueue.enqueue(s[i])
    
    # popping and dequeuing to compare the letters from the 
    # begging to end and end to beginning
    while myQueue.isEmpty() == False:
        if myStack.pop() != myQueue.dequeue():
            return False
    return True

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    return
