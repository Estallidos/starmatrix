from bisect import bisect

class Expelled:

    elements_list = ["H", "D", "He3", "He4", "C12", "O16",
                    "N14p", "C13", "n.r.", "Ne", "Mg", "Si",
                    "S", "Ca", "Fe", "remnants", "C13s", "N14s"]
    mass_points = []
    by_mass = {}

    def __init__(self, expelled_elements_filename = "expelled_elements"):
        self.read_expelled_elements_file(expelled_elements_filename)

    def read_expelled_elements_file(self, filename):
        """
        Reads a file of expelled elements per stellar mass.
        The file should include a row of data for each stellar mass.
        Structure of each row should be:
            - First column: stellar mass
            - 2nd to 19th columns: expelled mass of element i
                where i is in this list:
                ["H", "D", "He3", "He4", "C12", "O16",
                 "N14primary", "C13", "n.r.", "Ne", "Mg", "Si",
                 "S", "Ca", "Fe", "remnants", "C13secondary", "N14secondary"]

        """

        expelled_data = open(filename, "r")

        for line in expelled_data:
            data_row = [max(0.0, float(data)) for data in line.split()]
            mass = data_row.pop(0) # the first column is the mass
            self.mass_points.append(mass)
            self.by_mass[mass] = dict(zip(self.elements_list, data_row))

        expelled_data.close()

    def for_mass(self, m):
        """
        Interpolates expelled mass for all elements for a given stellar mass,
        using the data from the class' expelled_elements input file.

        """

        index = bisect(self.mass_points, m)
        mass_prev = self.mass_points[index - 1]
        mass_next = self.mass_points[index]
        elements_prev = self.by_mass[mass_prev]
        elements_next = self.by_mass[mass_next]
        interpolations = {"mass": m}
        p = (mass_next - m) / (mass_next - mass_prev)

        for element in self.elements_list:
            d = elements_next[element] - elements_prev[element]
            interpolations[element] = (elements_next[element] - (p * d) ) / m

        return interpolations