# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call
# the Queue methods on random input in a
# semi-random fashion. for instance, if
# you wanted to randomly decide between
# calling enqueue and dequeue, you would
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue,
# and checkRep methods several thousand
# times each.

import array
import random


class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self, x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail - self.head) == self.size
        if self.tail < self.head:
            assert (self.head - self.tail) == (self.max - self.size)
        if self.head == self.tail:
            assert (self.size == 0) or (self.size == self.max)

# Write a random tester for the Queue class.


def test_queue_empty(q):
    q.checkRep()
    assert q.empty()
    q.checkRep()
    assert not q.full()
    q.checkRep()
    assert None == q.dequeue()
    q.checkRep()


def test_queue_full(q):
    q.checkRep()
    assert not q.empty()
    q.checkRep()
    assert q.full()
    q.checkRep()
    assert not q.enqueue(12)
    q.checkRep()


def test_enqueue(q, i):
    assert q.enqueue(i)
    q.checkRep()
    assert not q.empty()
    q.checkRep()


def test_dequeue(q, i, j):
    assert j == q.dequeue()
    q.checkRep()
    assert not q.full()
    q.checkRep()


def test_queue(q, s):
    test_queue_empty(q)
    oracle = []
    for i in range(s * s):
        if random.choice([True, False]) and not q.full():
            test_enqueue(q, i)
            oracle.append(i)
        elif not q.empty():
            test_dequeue(q, i, oracle[0])
            oracle = oracle[1:]
    while not q.empty():
        test_dequeue(q, i, oracle[0])
        oracle = oracle[1:]
    test_queue_empty(q)
    for i in range(s):
        test_enqueue(q, i)
        oracle.append(i)
    test_queue_full(q)
    while not q.empty():
        test_dequeue(q, i, oracle[0])
        oracle = oracle[1:]
    test_queue_empty(q)


def test():
    n = 100000000
    for s in range(-n, 1):
        try:
            q = Queue(s)
        except:
            continue
        else:  # pragma: no cover
            print "A invalid queue was created with size equal to " + str(s)
    for s in range(1, n):
        q = Queue(s)
        test_queue(q, s)

test()
