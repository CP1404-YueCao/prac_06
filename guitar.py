CURRENT_YEAR = 2021
VINTAGE_AGE = 50

class Guitar:
    """Store details of guitars"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of a guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar"""
        return CURRENT_YEAR - self.year

    

