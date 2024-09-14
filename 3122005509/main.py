import sys
import jieba
from collections import Counter

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def preprocess(text):
    # 使用jieba进行中文分词
    words = jieba.lcut(text)
    return words

def calculate_similarity(words1, words2):
    # 计算词频
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # 计算交集和并集
    intersection = counter1 & counter2
    union = counter1 | counter2

    # 计算Jaccard相似度
    similarity = intersection.keys().__len__() / union.keys().__len__() if union.keys().__len__() else 0

    return similarity

def main(original_file, plagiarism_file, output_file):
    original_text = read_file(original_file)
    plagiarism_text = read_file(plagiarism_file)
    words1 = preprocess(original_text)
    words2 = preprocess(plagiarism_text)
    similarity = calculate_similarity(words1, words2)
    plagiarism_rate = similarity * 100  # 转换为百分比

    # 写入结果到文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"{plagiarism_rate:.2f}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <original_file> <plagiarism_file> <output_file>")
        sys.exit(1)

    original_file = sys.argv[1]
    plagiarism_file = sys.argv[2]
    output_file = sys.argv[3]

    main(original_file, plagiarism_file, output_file)
