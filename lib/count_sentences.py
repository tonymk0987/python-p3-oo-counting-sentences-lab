class MyString:
    def __init__(self, value=123):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Replaces exclamation marks and question marks with periods
        normalized_string = self.value.replace("?", ".").replace("!", ".")
        # # Split the string into sentences using periods as separators
        sentences = normalized_string.split(".")
        # Excludes empty strings from the count (resulting from consecutive periods)
        return len([sentence for sentence in sentences if sentence.strip() != ""])
