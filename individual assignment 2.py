class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def isCompleted(self):
        return self.completed

    def markCompleted(self):
        self.completed = True


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    def addToDo(self, task):
        new_node = Node(task)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def markToDoAsCompleted(self, title):
        current = self.head
        while current:
            if current.task.getTitle() == title:
                current.task.markCompleted()
                return
            current = current.next
        print("Task not found in the to-do list.")

    def viewToDoList(self):
        if self.head is None:
            print("To-do list is empty.")
        else:
            current = self.head
            while current:
                task = current.task
                status = "Completed" if task.isCompleted() else "Not Completed"
                print("Title:", task.getTitle())
                print("Description:", task.getDescription())
                print("Status:", status)
                print("--------------")
                current = current.next


# Example usage:
to_do_list = ToDoList()

task1 = Task("monday's task", "studying")
task2 = Task("tuesday.s task", "working on an assignment")

to_do_list.addToDo(task1)
to_do_list.addToDo(task2)

to_do_list.viewToDoList()
print("------------------------")

to_do_list.markToDoAsCompleted("monday's task")

to_do_list.viewToDoList()
print("------------------------")

to_do_list.markToDoAsCompleted("Task 4")