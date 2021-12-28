class ProgrammingLanguage:
    """Display information about a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return strings of ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
    