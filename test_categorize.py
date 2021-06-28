import unittest
from categorize import check_file_valid, process_count_categories

class test_check_file_valid(unittest.TestCase):
    def test_exists(self):
        try:
            check_file_valid('ip.tsv')
        except ValueError:
            self.fail("check_file_valid('ip.tsv') raised ExceptionType unexpectedly!")

    def test_failure(self):
        with self.assertRaises(ValueError):
            check_file_valid('ipv.tsv')


class test_process_count_categories(unittest.TestCase):
    def test_one_data(self):
        # region :: TEST VALUES
        test_values = [{
            "input": [ '320\tNamrata\tteen\n' ],
            "expected": { 'teen': 1 }
        }, {
            "input": [ '331\tAruna\tkid(3-5)\n' ],
            "expected": { 'kid(3-5)':1, }
        }, {
            "input": [ '342\tDilip\tkid(10+)\n' ],
            "expected": { 'kid(10+)': 1 }
        }, {
            "input": [ '320\tNamrata\tteen' ],
            "expected": { 'teen': 1 }
        }, {
            "input": [ '331\tAruna\tkid(3-5)' ],
            "expected": { 'kid(3-5)':1, }
        }, {
            "input": [ '342\tDilip\tkid(10+)' ],
            "expected": { 'kid(10+)': 1 }
        }]
        # endregion
        for i, testArguments in enumerate(test_values):
            with self.subTest(i = i):
                op = process_count_categories(testArguments["input"])
                self.assertEqual(testArguments["expected"], op)


    def test_multi_data(self):
        # region :: TEST VALUES
        test_values = [{
            "input": ['1\tPriya\tkid(3-5),kid(10+)\n'],
            "expected": {
                'kid(3-5)':1,
                'kid(10+)': 1
            }
        },{
            "input": ['408\tMadhura\tteen\n', '419\tDeepti\tkid(3-5)\n',],
            "expected": {
                'kid(3-5)':1,
                'teen': 1
            }
        },{
            "input": ['1\tPriya\tkid(3-5),kid(10+)'],
            "expected": {
                'kid(3-5)':1,
                'kid(10+)': 1
            }
        },{
            "input": ['408\tMadhura\tteen', '419\tDeepti\tkid(3-5)'],
            "expected": {
                'kid(3-5)':1,
                'teen': 1
            }
        }]
        # endregion
        for i, testArguments in enumerate(test_values):
            with self.subTest(i = i):
                op = process_count_categories(testArguments["input"])
                self.assertEqual(testArguments["expected"], op)


if __name__ == "__main__":
    unittest.main()