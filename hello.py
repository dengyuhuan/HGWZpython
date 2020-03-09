# coding:UTF-8
from collections import deque
squares = [1,2,334,23,234,23]
print((squares))
queue = deque(squares)
print(queue)
queue.append('a')
queue.append('b')
print(queue)
print(queue.popleft())
print(queue.popleft())

list = [x*10 for x in range(10)]
print(list)