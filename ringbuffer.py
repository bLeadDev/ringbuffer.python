
class Ringbuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        
    # Returns the number of elements stored in the ring.
    def get_number_of_elements(self):        
        pass 
    
    # Add an element to the ringbuffer. If the buffer is full, the oldest element is overwritten.
    def add(self, element):
        pass

    # Returns the oldest element in the ringbuffer and removes it from the buffer.
    def remove(self):
        pass
