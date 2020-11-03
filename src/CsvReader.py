import csv
from absolutepath import absolutepath


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    # setting-up property "data" as a list
    data = []

    def __init__(self, filepath):
        self.data = []
        # opening the CSV file as text data
        with open(absolutepath(filepath)) as text_data:
            # reading the CSV file as dictionary data strucuture
            csv_data = csv.DictReader(text_data, delimiter=',')

            # displaying the contents of the CSV file
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_Objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects