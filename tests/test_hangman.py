import sys
from hangman import hangman


class MyInput:
    def __init__(self, input_values):
        self.__input_values = input_values

    def readline(self):
        return self.__input_values.pop(0)


def test_hangman(capsys):
    sys.stdin = MyInput(list("abeolhxyznmo"))

    def test_hangman_hello_won_p():
        hangman.hangman(["hello"])

        out, err = capsys.readouterr()

        assert "You won!" in out

        expected = "".join(["Guess a letter:\n",
                            "Missed, mistake 1 out of 5\n",
                            "The word: *****\n",
                            "Guess a letter:\n",
                            "Missed, mistake 2 out of 5\n",
                            "The word: *****\n",
                            "Guess a letter:\n",
                            "Hit!\n",
                            "The word: *e***\n",
                            "Guess a letter:\n",
                            "Hit!\n",
                            "The word: *e**o\n",
                            "Guess a letter:\n",
                            "Hit!\n",
                            "The word: *ello\n",
                            "Guess a letter:\n",
                            "Hit!\n",
                            "The word: hello\n",
                            "You won!\n"])
        assert out == expected

        assert err == ''

    def test_hangman_lost_n():
        hangman.hangman(["hello"])

        out, err = capsys.readouterr()

        assert "You lost!" in out
        expected = "".join(["Guess a letter:\n",
                            "Missed, mistake 1 out of 5\n",
                            "The word: *****\n",
                            "Guess a letter:\n",
                            "Missed, mistake 2 out of 5\n",
                            "The word: *****\n",
                            "Guess a letter:\n",
                            "Missed, mistake 3 out of 5\n",
                            "The word: *****\n",
                            "Guess a letter:\n",
                            "Missed, mistake 4 out of 5\n",
                            "The word: *****\n",
                            "Guess a letter:\n",
                            "Missed, mistake 5 out of 5\n",
                            "The word: *****\n",
                            "You lost!\n"])

        assert out == expected

        assert err == ''

    test_hangman_hello_won_p()
    test_hangman_lost_n()
