class Stack:
    def __init__(self, size=10):  
        if size <= 0:
            raise ValueError("Размер стека должен быть положительным")
        self.size = size
        self.stack = [None] * size
        self.top_index = -1  

    def push(self, value):
        if self.top_index == self.size - 1:
            print("Ошибка: Стек переполнен")
            return  
        self.top_index += 1
        self.stack[self.top_index] = value


    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        value = self.stack[self.top_index]
        self.top_index -= 1
        return value

    def top(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.stack[self.top_index]

    def is_empty(self):
        return self.top_index == -1

    def __str__(self): 
        if self.is_empty():
            return "[]"
        return str(self.stack[:self.top_index + 1])



if __name__ == "__main__":
    stack = Stack(3)

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)  

    stack.push(40) # Ошибка: Стек переполнен

    print(stack.pop())  # 30
    print(stack.pop())  # 20
    print(stack.pop())  # 10

    try:
        stack.pop()  # Ошибка: Стек пуст
    except IndexError as e:
        print(f"Ошибка: {e}")

