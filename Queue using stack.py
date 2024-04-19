class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, item):
        self.stack1.append(item)
        print(f"Enqueued item: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue item.")
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            item = self.stack2.pop()
            print(f"Dequeued item: {item}")
        else:
            item = self.stack2.pop()
            print(f"Dequeued item: {item}")

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:")
            if len(self.stack2) > 0:
                for item in reversed(self.stack2):
                    print(item)
            for item in self.stack1:
                print(item)


# Usage example:
queue = QueueUsingStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.dequeue()
queue.display()