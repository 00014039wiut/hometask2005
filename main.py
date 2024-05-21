class Fibonacci:
    def __init__(self):
        self.start = 0
        self.first_difference = 1

    def __iter__(self):
        return self

    def __next__(self):
        next_number = self.start
        self.start = self.first_difference
        self.first_difference = self.start + next_number
        return next_number


fibo = Fibonacci()
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))

# for i in fibo:
#    print(i)
