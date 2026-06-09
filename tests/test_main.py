import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import main


def test_single_test_letter():
    assert main("א") == 1
    assert main("ת") == 400


def test_single_test_word():
    assert main("אבג") == 6
    assert main("שלום") == 376
    assert main("אלינור") == 297


def test_empty_string():
    assert main("") == 0


def test_with_spaces_and_punctuation():
    assert main("שלום עולם!") == 522
    assert main("מה שלומך?yy") == 441


def test_with_non_gematria_characters():
    assert main("שלום123") == 376
    assert main("!@#$%&*()") == 0


def test_sofit_letters():
    assert main("ך") == 20
    assert main("אן") == 51
