"""Module providing a library to read HRF file from Hattrick Organizer."""


class HrfEntry:
    """Class representing an entry in HRF File"""
    id = ""
    value = ""

    def print(self):
        print("=>" + self.id + "=" + self.value)

class HrfCategory:
    """Class representing a category in HRF File"""
    id = ""
    entries = dict()

    def print(self):
        print("***************" + self.id + "***************")
        for value in self.entries.values():
            value.print()
class HrfFile:
    """Class representing an HRF File"""
    categories = dict()

    def read(self, filename):
        file = open(filename, 'r')
        file_lines = file.readlines()
        current_category = None
        for file_line in file_lines:
            if len(file_line.strip()) > 0:
                if file_line.startswith('['):
                    category = HrfCategory()
                    category.id = file_line.replace("[", "").replace("]", "")
                    self.categories[category.id] = category
                    current_category = category
                else:
                    if current_category is not None:
                        values = file_line.split("=")
                        if len(values) == 2:
                            entry = HrfEntry()
                            entry.id = values[0]
                            entry.value = values[1]
                            current_category.entries[entry.id] = entry

        file.close()

    def print(self):
        for category in self.categories.values():
            category.print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hrf_file = HrfFile()
    hrf_file.read('D:/2126309-2024-02-10.hrf')
    hrf_file.print()
