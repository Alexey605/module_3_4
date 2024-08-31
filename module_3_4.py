def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        root_word = root_word.lower()
        new_ow = [x.lower() for x in other_words]
        if root_word in new_ow[i] or new_ow[i] in root_word:
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
