password_generator.py will create a secure ASCII password with a given length

How to run your program and any necessary dependencies.

To get started:
python3 password_generator.py

Then input the desired length of password. Inputted length must be a non-negative signed int

This tool is for educational use only and should not be used for actual password generation.

By the way the generator is implemented, if a malicious attacker could find a way to predict the seed of the .choice() function provided by the secrets python module, it would be incredibly easy to recreate generated passwords if they knew the length of the password they were trying to recreate.