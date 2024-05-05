


def count_word_frequency(text):
    #Функция для подсчета частоты слов в тексте
    words = text.split()
    word_frequency = {}

    for word in words:
        word = word.lower()
        word = word.strip('.,!?"\'')  # Удаляем знаки пунктуации
        if word:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    return word_frequency


user_text = input("Введите текст для анализа: ")
frequencies = count_word_frequency(user_text)
print("Частота слов в тексте:")
for word, frequency in frequencies.items():
    print(f"{word}: {frequency}")
