
class Ringbuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._count = 0
        self._vals = [None] * capacity
        self._write = 0
        self._read = 0
        
    # Returns the number of elements stored in the ring.
    def get_number_of_elements(self):        
        return self._count
    
    # Add an element to the ringbuffer. If the buffer is full, the oldest element is overwritten.
    def add(self, element):
        self._count += 1
        if self._count > self._capacity:
            self._count -= 1
        self._vals[self._write] = element
        self._write = (self._write + 1) % self._capacity 


    # Returns the oldest element in the ringbuffer and removes it from the buffer.
    def remove(self):
        self._count -= 1
        retVal = self._vals[self._read]
        self._read = (self._read + 1) % self._capacity 
        return retVal
