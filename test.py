import unittest
def myfunc(n):
    d = list()
    for i in range(1, n+1):
        if i%3==0 or i%5==0:
            if i%3==0 and i%5!=0:
                d.append("fizz")
            elif i%5==0 and i%3!=0:
                d.append("buzz")
            else:
                d.append("fizzbuzz")
        else:
            d.append(str(i))
    data = " ".join(d)
    return data

class myfuncTest(unittest.TestCase):
    def setUp(self):
        self.data = "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz"
    def test_myfunc(self):
        self.assertEqual(myfunc(15), self.data)


suite = unittest.TestLoader().loadTestsFromTestCase(myfuncTest)
unittest.TextTestRunner(verbosity=2).run(suite)

#n = int(input("n="))
#print(myfunc(n))
