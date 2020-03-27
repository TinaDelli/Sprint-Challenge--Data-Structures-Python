class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None #BinarySearchTree
        self.right = None #BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)    
            return 
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)    
            return
        if value < self.value:
            self.left.insert(value)  
        else:
            self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False     
            return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self is None:
            return None
        if self.right is None:
            return self.value        
        return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left FIRST
        if self.left is not None:
            self.left.for_each(cb)
        # print ourselves
        cb(self.value) 
        # go right 
        if self.right is not None:
            self.right.for_each(cb)