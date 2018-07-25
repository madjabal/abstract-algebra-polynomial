# Rough Draft of Polynomial Object for the purposes of studying and manipulating field polynomials


class Polynomial:

    coefficients_d = {}
    coefficients_l = []
    highest_degree = 0
    field = 0

    def __init__(self, coefficients, field):

        # Checks for input type and edits the corresponding attribute, including highest degree
        if type(coefficients) == dict:
            for key in coefficients:
                if coefficients[key] == 0:
                    del key
            self.coefficients_d = coefficients
            self.highest_degree = max(self.coefficients_d)
        elif type(coefficients) == list:
            index = coefficients[coefficients.length - 1]
            while coefficients[index] != 0:
                coefficients = coefficients[:-1]
            self.coefficients_l = coefficients
            self.highest_degree = coefficients
        else:
            print("Error: coefficients must be input as a list or dictionary with key or index referring to the degree "
                  "of the variable")

        # Checks for field and modifies the corresponding attribute
        if field == 0:
            self.field = field
        elif type(field) != int:
            print("Error: field must be input as an integer, the field of reals is input as 0")
        elif len([i for i in range(1, field) if field % i == 0]) != 0 or field == 1:
            print("Error: the modulus of a field must be a prime number")
        elif len([i for i in range(1, field) if field % i == 0]) == 0:
            self.field = field
            # for

        # Fills in the remaining attribute (either coefficients_d or coefficients_l)
        if type(coefficients) == dict:
            for coef in range(self.highest_degree):
                if coef in self.coefficients_d:
                    self.coefficients_l.append(self.coefficients_d[coef])
                else:
                    self.coefficients_l.append(coef)
        elif type(coefficients) == list:
            for coef_i in range(self.coefficients_l):
                if self.coefficients_l[coef_i] != 0:
                    self.coefficients_d[coef_i] = self.coefficients_l[coef_i]

    # def __repr__(self):
    #     s = ""
    #     for coeff in self.coefficients_d:
    # ADJUST THE FIELD CREATION TO MODULUS THE COEFFICIENTS
