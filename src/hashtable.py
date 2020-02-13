# '''
# Linked List hash table key/value pair
# '''

# NODE
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# LIST
class LinkedList:
    def __init__(self, head=None, next_node=None):
        self.head = head
        self.next = next_node

    def add_to_head(self, node):
        if self.head is None:
            self.head = node

        node.next = self.head
        self.head = node

    def find_key(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next

        return None

    def remove(self, key):
        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
            else:
                current = current.next

        return None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys.
    '''
    def __init__(self, capacity):
        # Number of buckets in the hash table.
        # So the number of spots in the array/ultimately the length...
        self.capacity = capacity
        self.storage = [None] * capacity

    def __str__(self):
        return f"HashTable capacity: {self.capacity}, HashTable current storage: {self.storage}"


    def _hash(self, key):
        '''
        Hash an arbitrary key and returns an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash.

        OPTIONAL STRETCH: Research and implement DJB2.
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Get the index.
        index = self._hash_mod(key)

        # If it's empty at this index...
        if self.storage[index] is None:
            # Create a Linked List.
            self.storage[index] = LinkedList(LinkedPair(key, value))

        else:
            self.storage[index].add_to_head(LinkedPair(key, value))

            # # Grab what's at the index.
            # original = self.storage[index]
            # # Create a node at the index.
            # self.storage[index] = LinkedPair(key, value)
            # # What was originally at the index location is now
            # # next to the node.
            # self.storage[index].next = original        

        # Code below is not handling collisions.

        # # Is there something at that index location already?
        # # None means something isn't already there given how we 
        # # initialized.
        # if self.storage[index] is not None:
        #     print(f"WARNING: Collision has occured at {index}!")
            
        # else:
        # # Set the value at that index location.
        # # Store as a key, value pair as a tuple.
        #     self.storage[index] = (key, value)
        
        return


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Get the index.
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None
        else:
            self.storage[index].remove(key)

        # # Check to see if there is a value already at that
        # # index location. # If there isn't a value already there...
        # if self.storage[index] is not None:
        #     # If the key at that index matches our key...
        #     if self.storage[index][0] == key:
        #         # Becomes None when it's removed.
        #         self.storage[index] = None

        #     else:
        #         print(f"Collision has occured at {index}!")
            
        # else:
        #     print(f"WARNING: {key} not found.")
        
        return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get the index.
        index = self._hash_mod(key)
        
        if self.storage[index] is None:
            return None

        else:
            return self.storage[index].find_key(key)       
        
        
        # # If there is something at that index location...
        # if self.storage[index] is not None:
        #     # If the key at that index matches our key...
        #     if self.storage[index][0] == key:
        #         # Retrieve the value for that key.
        #         return self.storage[index][1]

        #     else:
        #         print(f"WARNING: Collision has occured at {index}!")
            
        # else:
        #     return None
        
        return


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Double the capacity.
        self.capacity = self.capacity * 2

        # Reinitialize the new storage.
        new_storage = [None] * self.capacity

        # Save the old storage.
        old_storage = self.storage[:]

        self.storage = new_storage
        
        for i in range(len(old_storage)):
            if old_storage[i] is not None:
                current = old_storage[i].head

                while current is not None:                    
                    self.insert(current.key, current.value)
                    current = current.next

        # # Save the old storage.
        # old_storage = self.storage
        # # Double the capacity.
        # self.capacity = self.capacity * 2
        # # Reinitialize the new storage.
        # self.storage = [None] * self.capacity
        # # Find a new home for all of the items.
        # for item in old_storage:
        #     if item is not None:
        #         # Insert into new storage.
        #         self.insert(item[0], item[1])


if __name__ == "__main__":

    # Create an instance with a size of 2.
    ht1 = HashTable(2)
    print(ht1)
    print("-----------")    

    ht1.insert("key1", "Hello")
    ht1.insert("key2", "Goodbye")
    print(ht1.storage)
    print("-----------")

    # ht1.remove("key1")
    # ht1.remove("key2")
    # print(ht1.storage)
    # print("-----------")

    print(ht1.retrieve("key1"))

    print("-----------")

    print(ht1.resize())
    
    # print(ht1.storage)

    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")