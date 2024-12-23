# Student class for holding the variables
class StudentRecord:
    def __init__(self, studentID, firstName, lastName, dept, interests, sex):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.dept = dept
        self.interests = interests
        self.sex = sex

    def __str__(self):
        return (f"{self.studentID}: {self.firstName} {self.lastName} | Department: {self.dept} | "
                f"Gender: {self.sex} | Hobbies: {', '.join(self.interests)}")

class Node:
    def __init__(self, profile):
        self.profile = profile
        self.leftChild = None
        self.rightChild = None

# Tree for Search Functions of Profile variables
class ProfileTree:
    def __init__(self):
        self.rootNode = None

    def Add(self, profile):
        if not self.rootNode:
            self.rootNode = Node(profile)
        else:
            self._AddNode(self.rootNode, profile)

    def _AddNode(self, currentNode, profile):
        if profile.dept < currentNode.profile.dept:
            if currentNode.leftChild is None:
                currentNode.leftChild = Node(profile)
            else:
                self._AddNode(currentNode.leftChild, profile)
        else:
            if currentNode.rightChild is None:
                currentNode.rightChild = Node(profile)
            else:
                self._AddNode(currentNode.rightChild, profile)

    def FindByDept(self, dept):
        return self._FindByDeptNode(self.rootNode, dept)

    def _FindByDeptNode(self, currentNode, dept):
        if currentNode is None:
            return []
        results = []
        if currentNode.profile.dept == dept:
            results.append(currentNode.profile)
        results.extend(self._FindByDeptNode(currentNode.leftChild, dept))
        results.extend(self._FindByDeptNode(currentNode.rightChild, dept))
        return results

    def FindBySex(self, sex):
        return self._FindBySexNode(self.rootNode, sex)

    def _FindBySexNode(self, currentNode, sex):
        if currentNode is None:
            return []
        results = []
        if currentNode.profile.sex == sex:
            results.append(currentNode.profile)
        results.extend(self._FindBySexNode(currentNode.leftChild, sex))
        results.extend(self._FindBySexNode(currentNode.rightChild, sex))
        return results

    def FindByID(self, studentID):
        return self._FindByIDNode(self.rootNode, studentID)

    def _FindByIDNode(self, currentNode, studentID):
        if currentNode is None:
            return None
        if currentNode.profile.studentID == studentID:
            return currentNode.profile
        leftResult = self._FindByIDNode(currentNode.leftChild, studentID)
        if leftResult:
            return leftResult
        return self._FindByIDNode(currentNode.rightChild, studentID)

    def GetAllProfiles(self):
        records = []
        self._TraverseInOrder(self.rootNode, records)
        return records

    def _TraverseInOrder(self, currentNode, records):
        if currentNode is not None:
            self._TraverseInOrder(currentNode.leftChild, records)
            records.append(currentNode.profile)
            self._TraverseInOrder(currentNode.rightChild, records)

# Search student profiles for hobbies
class InterestGraph:
    def __init__(self):
        self.graph = {}

    def AddRecord(self, profile):
        for interest in profile.interests:
            if interest not in self.graph:
                self.graph[interest] = []
            self.graph[interest].append(profile)

    def SearchByInterest(self, interest):
        return self.graph.get(interest, [])

# main function
if __name__ == "__main__":
    studentTree = ProfileTree()
    hobbyGraph = InterestGraph()

    while True:
        print("\n1. Add Student Profile")
        print("2. Search by Department")
        print("3. Search by Hobby")
        print("4. Search by Gender")
        print("5. Search by Student ID")
        print("6. List All Profiles")
        print("7. Exit")
        action = input("Select an action: ")

        if action == "1":
            studentID = int(input("Student ID: "))
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            sex = input("Gender (m for Male, f for Female): ").strip().lower()

            if sex not in ('m', 'f'):
                print("Invalid input for gender. Use 'm' or 'f'.")
                continue

            dept = input("Department: ")
            interests = input("Hobbies (use ',' to split hobbies): ").split(",")
            interests = [h.strip() for h in interests]

            newProfile = StudentRecord(studentID, firstName, lastName, dept, interests, sex)
            studentTree.Add(newProfile)
            hobbyGraph.AddRecord(newProfile)

            print("Profile successfully added!")

        elif action == "2":
            dept = input("Department to search: ")
            matches = studentTree.FindByDept(dept)

            if matches:
                print(f"\nStudents in {dept}:")
                for entry in matches:
                    print(entry)
            else:
                print(f"No students found in {dept}.")

        elif action == "3":
            interest = input("Hobby to search: ")
            matches = hobbyGraph.SearchByInterest(interest)

            if matches:
                print(f"\nStudents interested in {interest}:")
                for entry in matches:
                    print(entry)
            else:
                print(f"No students found with hobby {interest}.")

        elif action == "4":
            sex = input("Gender to search (m for Male, f for Female): ").strip().lower()

            if sex not in ('m', 'f'):
                print("Invalid input for gender. Use 'm' or 'f'.")
                continue

            matches = studentTree.FindBySex(sex)

            if matches:
                print(f"\nStudents with gender {sex}:")
                for entry in matches:
                    print(entry)
            else:
                print(f"No students found with gender {sex}.")

        elif action == "5":
            studentID = int(input("Enter Student ID: "))
            result = studentTree.FindByID(studentID)

            if result:
                print(f"\nStudent Found:\n{result}")
            else:
                print(f"No student found with ID {studentID}.")

        elif action == "6":
            allProfiles = studentTree.GetAllProfiles()
            if allProfiles:
                print("\nAll Profiles:")
                for profile in allProfiles:
                    print(profile)
            else:
                print("No profiles available.")

        elif action == "7":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid action. Try again.")
