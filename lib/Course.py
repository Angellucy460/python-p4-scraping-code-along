class Course:
    def __init__(self, title="", schedule="", description=""):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        output = ''
        output += f"Title: {self.title}\n"
        output += f"Schedule: {self.schedule}\n"
        output += f"Description: {self.description}\n"
        output += "------------------"
        return output
