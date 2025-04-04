class Stack:
    def __init__(self, limit=None):
        self._stack = []
        self.limit = limit  # Optional limit

    def push(self, value):
        if self.limit is not None and len(self._stack) >= self.limit:
            raise OverflowError("Stack is full")
        self._stack.append(value)

    def pop(self):
        if not self._stack:
            raise IndexError("Pop from empty stack")
        return self._stack.pop()

    def peek(self):
        if not self._stack:
            raise IndexError("Peek from empty stack")
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def empty(self):
        return len(self._stack) == 0

    def full(self):
        return self.limit is not None and len(self._stack) == self.limit

    def search(self, value):
        if value in self._stack:
            # Distance from top: 0 if top, 1 if second from top, etc.
            return len(self._stack) - 1 - self._stack[::-1].index(value)
        return -1

    def __str__(self):
        return f"Stack({self._stack})"
