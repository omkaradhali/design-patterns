"""

Single Responsibility Principle

"""
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        print("SELF\n")
        return "\n".join(self.entries)

    # break SRP
    def save(self, filename):
        # file = open(filename, "w")
        # file.write(str(self))
        # file.close()
        print(str(self))

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


# class PersistenceManager:
#     def save_to_file(journal, filename):
#         file = open(filename, "w")
#         file.write(str(journal))
#         file.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry("I cried today.")
    j.add_entry("I ate a bug.")
    j.save("something.txt")
    print(f"Journal entries:\n{j}\n")

# p = PersistenceManager()
# file = r'c:\temp\journal.txt'
# p.save_to_file(j, file)

# verify!
# with open(file) as fh:
#     print(fh.read())
