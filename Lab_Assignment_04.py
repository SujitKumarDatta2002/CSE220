class Patient:

    def __init__(self, id, name, age, blood, prev, next):
        self.id = id
        self.name = name
        self.age = age
        self.blood = blood
        self.prev = prev
        self.next = next


class WRM:

    def __init__(self) -> None:
        self.head = None
        self.temp = None

    def RegisterPatient(self, id, name, age, bloodgroup):
        p = Patient(id, name, age, bloodgroup, None, None)
        if self.head == None:
            self.head = p
            self.temp = self.head
        else:
            self.temp.next = p
            p.next = self.head
            p.prev = self.temp
            self.temp = p
            self.head.prev = p
        print("Success Registering Patient")

    def ServePatient(self):
        if self.head == None:
            return "No patient to be served."
        store = self.head.name
        if self.head.next == self.head:
            self.head = None
            self.temp = None
            return f"{store} is served."
        tail = self.head.next
        self.head.prev.next = tail
        self.head.prev = None
        self.head.next = None
        self.head = tail
        return f"{store} is served."

    def CancelAll(self):
        self.head = None
        self.temp = None
        print("All apoinment cancelled.")

    def CanDoctorGoHome(self):
        if self.head != None:
            return "No"
        return "Yes"

    def ShowAllPatient(self):
        if self.head != None:
            print(self.head.name, end=", ")
            if self.head.next != None:
                tail = self.head.next
                while tail != self.head and tail != None:
                    if tail.next == self.head:
                        print(tail.name)
                    else:
                        print(tail.name, end=", ")
                    tail = tail.next
                # print()
        else:
            print("No patient in wating room..!")

    def insertEnd(self, head, new_node):

        if (head == None):
            new_node.next = new_node
            new_node.prev = new_node
            head = new_node
            return head

        last = head.prev
        new_node.next = head
        head.prev = new_node
        new_node.prev = last
        last.next = new_node

        return head

    def ReverseTheLine(self):
        if (self.head == None):
            return "Nothing to be reversed"
        if self.head.prev == None:
            return "Nothing to be reversed"
        new_head = None
        last = self.head.prev
        curr = last
        while (curr.prev != last):
            prev = curr.prev
            new_head = self.insertEnd(new_head, curr)
            curr = prev
        new_head = self.insertEnd(new_head, curr)

        self.head = new_head
        return "Successfully reverse the line"


w = WRM()
print("**Welcome to waiting room management system**")

while True:
    print("==Choose your options==")
    print("1. RegisterPatient()")
    print("2. ServePatient()")
    print("3. CancelAll()")
    print("4. CanDoctorGoHome()")
    print("5. ShowAllPatient()")
    print("6. ReverseTheLine()")
    print("7. exit")
    print("====================")
    user = int(input("Enter your choice: "))
    if user == 1:
        print("Executing RegisterPatient().......")
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        blood = input("Enter blood group: ")
        w.RegisterPatient(id, name, age, blood)
    elif user == 2:
        print("Executing ServePatient().......")
        print(w.ServePatient())
    elif user == 3:
        print("Executing CancelAll()........")
        w.CancelAll()
    elif user == 4:
        print("Executing CanDoctorGoHome()........")
        print(w.CanDoctorGoHome())
    elif user == 5:
        print("Executing ShowAllPatient()........")
        w.ShowAllPatient()
    elif user == 6:
        print("Executing ReverseTheLine()........")
        print(w.ReverseTheLine())
    elif user == 7:
        print("Thanks for using waiting room management system")
        print("Exiting......")
        w = None
        w = WRM()
        break
    else:
        print("No such option")
# w.RegisterPatient(1001, "Sujit", 21, "A+")
# w.RegisterPatient(1002, "Kumar", 22, "B+")
# w.ShowAllPatient()
# print(w.ServePatient())
# w.ShowAllPatient()
# w.CancelAll()
# w.ShowAllPatient()
# print(w.CanDoctorGoHome())


# print("............Test case 2..........")
# w2 = WRM()
# w2.RegisterPatient(1003, "Loren", 21, "A+")
# w2.RegisterPatient(1004, "Sofia", 22, "B+")
# w2.ShowAllPatient()
# # new = w2.reverse(w2)
# w2.reverse()
# # print(w2.ServePatient())
# w2.ShowAllPatient()
# print(w2.ServePatient())
# w2.ShowAllPatient()
# print(w2.CanDoctorGoHome())
