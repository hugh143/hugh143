import unittest
from unittest.mock import patch, mock_open
import main

class TestPlagiarismChecker(unittest.TestCase):
    def test_read_file(self):
        test_content = "这是测试文本。"
        with patch('builtins.open', mock_open(read_data=test_content)) as mocked_file:
            result = main.read_file('test.txt')
            mocked_file.assert_called_once_with('test.txt', 'r', encoding='utf-8')
            self.assertEqual(result, test_content)

    def test_preprocess(self):
        test_text = "今天，天气 真好。"
        expected_result = ['今天', '天气', '真','好']
        result = main.preprocess(test_text)
        self.assertEqual(result, expected_result)

    def test_calculate_similarity(self):
        words1 = ['今天', '天气', '不错']
        words2 = ['天气', '不错', '今天']
        similarity = main.calculate_similarity(words1, words2)
        self.assertEqual(similarity, 1.0)

        words1 = ['今天', '测试']
        words2 = ['测试', '数据']
        similarity = main.calculate_similarity(words1, words2)
        self.assertAlmostEqual(similarity, 0.333333333)

    def test_main_flow(self):
        with patch('main.read_file', return_value='今天天气不错。') as mock_read_file:
            with patch('main.preprocess', return_value=['今天', '天气', '不错']) as mock_preprocess:
                with patch('main.calculate_similarity', return_value=0.6) as mock_calculate_similarity:
                    with patch('builtins.open', new_callable=mock_open) as mock_file:
                        main.main('orig.txt', 'plagiarism.txt', 'output.txt')
                        mock_file().write.assert_called_once_with('60.00\n')


if __name__ == '__main__':
    unittest.main()