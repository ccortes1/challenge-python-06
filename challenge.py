def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    # You have to code here!
    def division(x):
        return x/n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def test_closure_make_division_by(self):
            # Make the closure test here
            num = {6:[3,18], 20:[5,100], 3:[18,54]}
            for key, value in num.items():
                division = make_division_by(value[0])
                self.assertEqual(division(value[1]), key)
    
    run()
