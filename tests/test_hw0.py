import pytest
import sys
import os

# Add the parent directory to the path so we can import hw0
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the hw0 module to test the variables
import hw0

def test_spongebob_variable_exists():
    """Test that the 'sb' variable exists in the code."""
    assert hasattr(hw0, 'sb'), "Variable 'sb' should be defined in your code"

def test_spongebob_is_string():
    """Test that sb variable is a string (not a number or other type)."""
    assert isinstance(hw0.sb, str), f"Variable 'sb' should be a string, but got {type(hw0.sb).__name__}"

def test_spongebob_exact_value():
    """Test that sb is exactly 'spongebob' (all lowercase)."""
    assert hw0.sb == "spongebob", f"Expected 'spongebob' but got '{hw0.sb}'"

def test_spongebob_not_capitalized():
    """Test that sb is not capitalized (this catches the common mistake)."""
    assert hw0.sb != "Spongebob", "Variable 'sb' should be 'spongebob' (lowercase), not 'Spongebob'"
    assert hw0.sb != "SpongeBob", "Variable 'sb' should be 'spongebob' (lowercase), not 'SpongeBob'"
    assert hw0.sb != "SPONGEBOB", "Variable 'sb' should be 'spongebob' (lowercase), not 'SPONGEBOB'"

def test_spongebob_no_extra_spaces():
    """Test that there are no extra spaces around the name."""
    assert hw0.sb.strip() == hw0.sb, f"Variable 'sb' should not have extra spaces. Got: '{hw0.sb}'"
    assert hw0.sb == hw0.sb.strip(), "Remove any extra spaces from your 'sb' variable"

def test_spongebob_length():
    """Test that the string has the right length."""
    expected_length = 9  # "spongebob" is 9 characters
    actual_length = len(hw0.sb)
    assert actual_length == expected_length, f"Expected 'spongebob' (9 characters) but got '{hw0.sb}' ({actual_length} characters)"

def test_spongebob_contains_correct_letters():
    """Test that sb contains all the right letters."""
    expected_letters = set("spongebob")
    actual_letters = set(hw0.sb.lower())
    missing_letters = expected_letters - actual_letters
    extra_letters = actual_letters - expected_letters
    
    assert not missing_letters, f"Your string is missing these letters: {missing_letters}"
    assert not extra_letters, f"Your string has these extra letters: {extra_letters}"

def test_spongebob_starts_with_s():
    """Test that the name starts with lowercase 's'."""
    assert hw0.sb.startswith('s'), f"Variable 'sb' should start with lowercase 's', but starts with '{hw0.sb[0]}'"

def test_spongebob_ends_with_b():
    """Test that the name ends with lowercase 'b'."""
    assert hw0.sb.endswith('b'), f"Variable 'sb' should end with lowercase 'b', but ends with '{hw0.sb[-1]}'"

def test_spongebob_not_empty():
    """Test that sb is not an empty string."""
    assert hw0.sb != "", "Variable 'sb' should not be empty"
    assert len(hw0.sb) > 0, "Variable 'sb' should not be empty"

def test_spongebob_not_none():
    """Test that sb is not None."""
    assert hw0.sb is not None, "Variable 'sb' should not be None"

def test_spongebob_no_numbers():
    """Test that sb doesn't contain any numbers."""
    assert not any(char.isdigit() for char in hw0.sb), f"Variable 'sb' should not contain numbers, but got '{hw0.sb}'"

def test_spongebob_no_special_characters():
    """Test that sb only contains letters (no punctuation, etc.)."""
    assert hw0.sb.isalpha(), f"Variable 'sb' should only contain letters, but got '{hw0.sb}'"

def test_spongebob_common_misspellings():
    """Test against common misspellings of spongebob."""
    common_mistakes = [
        "sponge bob",     # space in middle
        "spongbob",       # missing 'e'
        "spongebobb",     # extra 'b'
        "spongbobb",      # missing 'e' and extra 'b'
        "sponegbob",      # swapped letters
    ]
    
    for mistake in common_mistakes:
        assert hw0.sb != mistake, f"Close! But '{mistake}' is not quite right. Try 'spongebob'"

# This test will always pass - it's just to show what the correct value looks like
def test_show_correct_answer():
    """This test shows you what the correct answer should look like."""
    correct_answer = "spongebob"
    print(f"\n✅ The correct value for 'sb' is: '{correct_answer}'")
    print(f"📝 Your current value is: '{hw0.sb}'")
    print(f"🔍 Match? {hw0.sb == correct_answer}")
    
    assert True, "This test always passes - it just shows you the correct format!"