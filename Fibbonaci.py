class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a

limit = 10  
fibonacci_sequence = FibonacciIterator(limit)

print(f"Первые {limit} чисел Фибоначчи:")
for number in fibonacci_sequence:
    print(number)
