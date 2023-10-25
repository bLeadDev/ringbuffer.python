from ringbuffer import Ringbuffer

buffer_size = 10

def test_create_ringbuffer():
    #given an instantiated buffer
    rb = Ringbuffer(buffer_size)
    #when 

    #then the number of elements is zero
    assert rb.get_number_of_elements() == 0


def test_check_number_of_elements():
    #given an empty buffer
    rb = Ringbuffer(buffer_size)
    #when filled with 5 elemtns
    for i in range(5):
        rb.add(i)
    #the number of elements is 5
    assert rb.get_number_of_elements() == 5
    #when filled with another 5 elements
    for i in range(5):
        rb.add(i)
    #the number of elements is 10
    assert rb.get_number_of_elements() == 10

def test_it_should_report_the_correct_number_of_elements():
    #given a filled buffer with 3 elements
    rb = Ringbuffer(buffer_size)
    for i in range(3):
        rb.add(i)
    #when removing an element
    rb.remove()
    #then the count decreases to two
    assert rb.get_number_of_elements() == 2

def test_it_should_not_exceed_its_maximum_nbOfElements():
    #given a filled buffer
    rb = Ringbuffer(buffer_size)
    for i in range(buffer_size):
        rb.add(i)
    #when adding an element
    rb.add(10)
    #then the buffer is still at max and not exceeding
    assert rb.get_number_of_elements() == 10    

def test_it_should_return_the_before_pushed_values():
    #given a partially  filled buffer
    rb = Ringbuffer(buffer_size)
    for i in range(3):
        rb.add(i)

    #when removing the elements
    ret = rb.remove()
    #then the numbers get returned in inverted order  
    assert ret == 0  

    ret = rb.remove()
    assert ret == 1

    ret = rb.remove()
    assert ret == 2  

def test_it_should_return_the_before_pushed_values_full_test():
    #TEST IS NOT WOTRKING! NO IDEA WHY!!
    #given a fully filled buffer
    rb = Ringbuffer(buffer_size)
    for i in range(10):
        rb.add(i)
    #when removing element by element
    for i in range(10,0):
        ret = rb.remove()
        print(f"{ret}")
        #then the elements get returned in inverse order
        assert ret == i*2  

def test_it_should_return_false_when_empty():
    #TEST IS NOT WOTRKING! NO IDEA WHY!!
    #given an empty buffer
    rb = Ringbuffer(buffer_size)
    #when removing an element
    ret = int(32)
    ret = rb.remove()
    #None gets returned
    assert ret is None
    
def test_it_should_overwrite_the_last_element_when_buffer_is_full():
    #TEST IS NOT WOTRKING! NO IDEA WHY!!
    #given a fully filled buffer    
    rb = Ringbuffer(buffer_size)
    for i in range(10):
        rb.add(i)
    #when adding another element
    rb.add(10)
    #all other elements get returned in reverse order
    for i in range (11,1):
        assert i == rb.remove() 

