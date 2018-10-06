from hangman import hangman


def test_hangman(capsys):
    input_values = list("abeolhxyznmo")

    def mock_input(s):
        return input_values.pop(0)

    hangman.input = mock_input

    def test_hangman_hello_won_p():
        hangman.hangman(["hello"])

        out, err = capsys.readouterr()

        assert "You won!" in out

        expected = "".join(["Missed, mistake 1 out of 5\n",
                           "The word: *****\n",
                            "Missed, mistake 2 out of 5\n",
                            "The word: *****\n",
                            "Hit!\n",
                            "The word: *e***\n",
                            "Hit!\n",
                            "The word: *e**o\n",
                            "Hit!\n",
                            "The word: *ello\n",
                            "Hit!\n",
                            "The word: hello\n",
                            "You won!\n"])
        assert out == expected

        assert err == ''

    def test_hangman_lost_n():
        hangman.hangman(["hello"])

        out, err = capsys.readouterr()

        assert "You lost!" in out
        expected = "".join(["Missed, mistake 1 out of 5\n",
                            "The word: *****\n",
                            "Missed, mistake 2 out of 5\n",
                            "The word: *****\n",
                            "Missed, mistake 3 out of 5\n",
                            "The word: *****\n",
                            "Missed, mistake 4 out of 5\n",
                            "The word: *****\n",
                            "Missed, mistake 5 out of 5\n",
                            "The word: *****\n",
                            "You lost!\n"])

        assert out == expected

        assert err == ''

    test_hangman_hello_won_p()
    test_hangman_lost_n()
