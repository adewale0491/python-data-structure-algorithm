class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


x = Stack()

x.push('monkey')
x.push(23)

print(x.isEmpty())
print(x.size())
print(x.pop())
# print(x)


class myStack:
    def __init__(self):
        self.arr = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.arr[self.length - 1]

    def push(self, value):
        self.arr.append(value)
        self.length += 1

    def pop(self):
        popped_item = self.arr[self.length - 1]
        del self.arr[self.length - 1]
        self.length -= 1
        return popped_item

    def __contain_(self, item):
        return item in self.arr


estack = myStack()
estack.push('chickenRepublic')
estack.push('kfc')
estack.push('mybig')

print(estack)

estack.push('bestmeal')

print(estack)

estack.pop()

print(estack)

x = estack.peek()

print(x)

print(estack)