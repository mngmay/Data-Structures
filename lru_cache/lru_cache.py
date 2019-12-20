from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.max = limit
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.cache.move_to_front(node)
            return node.value[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if key exists, overwrite old value and move to front
        if key in self.storage:
            node = self.storage[key]
            node.value = {key: value}
            self.cache.move_to_front(node)
        else:
            # if at limit
            if self.cache.length == self.max:
                tail = self.cache.tail.value
                # remove oldest entry in the cache
                self.cache.remove_from_tail()
                # need key of tail
                for k in tail:
                    # delete from storage too
                    del self.storage[k]

            # move to front
            # adds to DLL cache
            self.cache.add_to_head({key: value})
            # adds to storage
            self.storage[key] = self.cache.head


'''
Lecture solution:

class LRUCache:

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()
'''
'''
    key == 'value1'
    value == 'a'

    LinkedListNode??Name prev == some other node, next == a different node value == ('value1', 'a')
'''
'''

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            # also works but not as readable/type more later self.order.move_to_end(self.storage[key])
            return node.value[1]
            # return self.storage[key].value[1]
        else:
            return None

    def set(self, key, value):
        
        # Check and see if key is in cache
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return 
        
        # Check the length, if at limit, delete last. 
        # If it is in the cache move to front and update value
        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            # you could do del self.storage[self.order.remove_from_head().value[0]] but it's harder to read so not recommended

            self.size -= 1



        # If not Add to the front of the cache
        # Defining tail as most recent and head as oldest
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1

'''
