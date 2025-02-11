from collections import deque

def word_ladder(start, end, word_list):
    word_set = set(word_list)
    queue = deque([(start, 1)])

    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + ch + word[i+1:]
                if next_word in word_set:
                    queue.append((next_word, steps + 1))
                    word_set.remove(next_word)
    return 0

print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Output: 5
