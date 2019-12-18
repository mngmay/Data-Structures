# Code with notes


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If inserting we must already have a tree/root
        # if value is less than self.value go left, make a new tree/node if empty, otherwise
        # keep going (recursion)
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
            # if greater than or equal to then go right, make a new tree/node if empty, otherwise
            # keep going (recursion)
        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target == self.value return it
        # otherwise go left or right based on smaller
        current = self
        while current:
            if target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right
            elif target == current.value:
                return True
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # call for_each on the current value
        cb(self.value)
        # if there is a left go left and call cb
        if self.left:
            self.left.for_each(cb)
        # if there is a right go right and call cb
        if self.right:
            self.right.for_each(cb)
