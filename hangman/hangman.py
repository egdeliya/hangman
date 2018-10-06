import random
from collections import Counter


def game_loop(max_tries, words):
    wasted_tries = 0
    word = words[random.randint(0, len(words) - 1)]
    game_is_won = False

    checker = check_letter(word)
    get_current_state = get_state(word)

    while wasted_tries < max_tries:
        letter = input("Guess a letter:\n")

        (is_in_word, game_is_won) = checker(letter)

        wasted_tries = get_current_state(is_in_word, letter,
                                         wasted_tries, max_tries)

        if game_is_won:
            break

    print_game_result(game_is_won)


def get_state(word):
    cur_word_state = ['*' for _ in range(len(word))]

    def get_current_state(is_in_word, letter, wasted_tries, max_tries):
        nonlocal cur_word_state
        if is_in_word:
            cur_word_state = [letter if word[i] == letter
                              else cur_word_state[i] for i in range(len(word))]
            print("Hit!")
        else:
            wasted_tries += 1
            print("Missed, mistake {tries} out of {max_tries}"
                  .format(tries=wasted_tries, max_tries=max_tries))

        print("The word: {cur_word_state}"
              .format(cur_word_state="".join(cur_word_state)))
        return wasted_tries

    return get_current_state


def check_letter(word):
    letters_counter = Counter(word)

    def checker(letter):
        accepted_letter = False
        game_is_won = False

        if letters_counter[letter] > 0:
            letters_counter.pop(letter)
            accepted_letter = True

            if len(letters_counter) == 0:
                game_is_won = True

        return accepted_letter, game_is_won

    return checker


def print_game_result(game_is_won):
    if game_is_won:
        print("You won!")
    else:
        print("You lost!")


def hangman(words=["hello", "world"]):
    max_tries = 5
    words = words

    game_loop(max_tries, words)


if __name__ == "__main__":
    hangman()
