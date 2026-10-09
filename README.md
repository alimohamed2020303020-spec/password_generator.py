# Password Generator

A simple command-line password generator written in Python. It builds a random password from letters, numbers, and symbols using the `secrets` module, which is designed for security-sensitive randomness.

## Features

- Random passwords from uppercase and lowercase letters, numbers, and special symbols
- Minimum length of 8 characters
- Input validation: asks again if you type something that is not a number
- Uses `secrets` instead of `random` for stronger randomness

## Requirements

- Python 3.6 or newer (no external libraries needed)

## How to Run

```bash
python password_generator.py
```

Then enter the length you want for your password.

## Example

```
================== Password Generator ==================

How long do you want your password to be: 12
k7#Qe3∆mT9@x
```

## How It Works

1. All allowed characters are combined into one string.
2. The program asks for the password length and repeats the question until the input is a number that is at least 8.
3. `secrets.choice` picks one random character at a time, `length` times, and the characters are joined into the final password.

## Ideas for Improvement

- Guarantee at least one letter, one number, and one symbol in every password
- Let the user choose which character types to include
- Copy the generated password to the clipboard

## License

Free to use for learning and personal projects.
