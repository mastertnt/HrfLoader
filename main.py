"""Module providing a library to read HRF file from Hattrick Organizer."""
import dataclasses
from pprint import pformat


@dataclasses.dataclass
class HrfEntry:
    """Class representing an entry in HRF File"""
    id = ""
    value = ""

    def __repr__(self):
        return pformat(vars(self), indent=4, width=1)


@dataclasses.dataclass
class HrfCategory:
    """Class representing a category in HRF File"""
    id = ""
    entries = {}

    def __repr__(self):
        result = ""
        result += "***************" + self.id + "***************";
        for value in self.entries.values():
            result += value
        return result


class HrfFile:
    """Class representing an HRF File"""
    categories = {}

    def read(self, filename):
        """Function to read an HRF file"""
        with open(filename, "r", encoding="utf8") as file:
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

    def __repr__(self):
        result = ""
        for category in self.categories.values():
            result += category
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hrf_file = HrfFile()
    hrf_file.read('D:/2126309-2024-02-10.hrf')
    print(hrf_file)
