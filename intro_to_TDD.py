import unittest

# 1. reverseList
def reverseList(arr):
    for i in range(0, int(len(arr)/2)):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    return arr

# 2. isPalindrome
def isPalindrome(str):
    for j in range(int(len(str)/2)):
        if str[j] != str[len(str)-1-j]:
            return False
    return True

# 3. coins
def coin(num):
    change = []
    count_quarter = 0
    count_dime = 0
    count_nickel = 0
    count_penny = 0

    while num > 0:
        if num >= 25:
            num -= 25
            count_quarter += 1
        elif num >= 10:
            num -= 10
            count_dime += 1
        elif num >= 5:
            num -= 5
            count_nickel += 1
        else:
            num -= 1
            count_penny += 1
        
    change.append(count_quarter)
    change.append(count_dime)
    change.append(count_nickel)
    change.append(count_penny)
    
    return change

# 4. factorial
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

# 5. fibonacci
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

class ReverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def testThree(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])
    def testFour(self):
        self.assertEqual(reverseList([1,3,5,7]), [7,5,3,1])
    def testFive(self):
        self.assertEqual(reverseList([2,4,6,8]), [8,6,4,2])
    def setUp(self):
        print('running setUp')
    def tearDown(self):
        print('running teardown tasks')

class IsPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome('racecar'))
    def testTwo(self):
        self.assertFalse(isPalindrome('rcbar'))
    def testThree(self):
        self.assertTrue(isPalindrome('madam'))
    def testFour(self):
        self.assertFalse(isPalindrome('school'))
    def testFive(self):
        self.assertTrue(isPalindrome('noon'))
    def testSix(self):
        self.assertFalse(isPalindrome('motor'))
    def testSeven(self):
        self.assertTrue(isPalindrome('rotor'))
    def setUp(self):
        print('running setUp')
    def tearDown(self):
        print('running teardown tasks')

class CoinTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coin(87), [3,1,0,2])
    def testTwo(self):
        self.assertEqual(coin(50), [2,0,0,0])
    def testThree(self):
        self.assertEqual(coin(43), [1,1,1,3])
    def testFour(self):
        self.assertEqual(coin(57), [2,0,1,2])
    def testFive(self):
        self.assertEqual(coin(17), [0,1,1,2])
    def testSix(self):
        self.assertEqual(coin(7), [0,0,1,2])    
    def setUp(self):
        print('running setUp')
    def tearDown(self):
        print('running teardown tasks')

class factorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(4), 24)
    def testTwo(self):
        self.assertEqual(factorial(5), 120)
    def testThree(self):
        self.assertEqual(factorial(6), 720)
    def testFour(self):
        self.assertEqual(factorial(7), 5040) 
    def setUp(self):
        print('running setUp')
    def tearDown(self):
        print('running teardown tasks')

class fibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(5), 3)
    def testTwo(self):
        self.assertEqual(fibonacci(4), 2)
    def testThree(self):
        self.assertEqual(fibonacci(6), 5)
    def testFour(self):
        self.assertEqual(fibonacci(10), 34)
    
    def setUp(self):
        print('running setUp')
    def tearDown(self):
        print('running teardown tasks')

if __name__ == '__main__':
    unittest.main()