class Person:

    def __init__(self, head, tounge):
        self.head = head
        self.tounge = tounge

    def behading(self):
        if self.head == "green" and self.tounge == "red":
            print ("Person has behaded")
        else:
            print ("Person remains alive")


person = Person(head="green", tounge="red")
person.behading()
