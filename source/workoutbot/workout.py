from random import choice
from re import compile


class Exercise:
    def __init__(self, name, reps, link=None, description=None, difficulty=None):
        self.name = name
        self.reps = reps
        self.link = link
        self.description = description
        self.difficulty = difficulty


class Workout:
    def pick_exercise(self):
        """ Return a base exercise. """
        return choice(self.exercises)

    def pick_explosive(self):
        """ Return an explosive exercise. """
        return choice(self.explosive)

    def pick_additional(self):
        """ Return an additional exercise. """
        if self.additional: return choice(self.additional)

    def __init__(self, exercises, explosive, additional):
        self.exercises = exercises
        self.explosive = explosive
        self.additional = additional
        self.exercise_choice = self.pick_exercise()
        self.explosive_choice = self.pick_explosive()
        self.additional_choice = self.pick_additional()

    def group(self):
        """ Return all base exercises for a muscle group (includes: name, difficulty, link). """
        group_list = []
        difficulty_weight = {'Easy': 1, 'Medium': 2, 'Hard': 3}
        for exercise in self.exercises:
            group_list.append(
                f"{exercise.name} | <b>{exercise.difficulty.capitalize()}</b>" + f"\n{exercise.link}\n\n")

        r = compile('<b>(.*)</b>')
        return "".join(sorted(group_list, key=lambda x: difficulty_weight[r.search(x).group(1)]))

    def fetch_workout(self):
        """ Return a workout that contains 2-3 exercises: base, explosive, additional (optional). """
        delimiter = "\n______________________________\n\n"

        # ========================================================================================= 1st exercise
        exercise_context = f"<b>EXERCISE 1:</b> {self.exercise_choice.name} - {choice(self.exercise_choice.reps)}."
        if self.exercise_choice.description: exercise_context += f"\n<i>{self.exercise_choice.description}</i>"
        if self.exercise_choice.link: exercise_context += f"\n{self.exercise_choice.link}"

        # ========================================================================================= 2nd exercise
        explosive_context = f"<b>EXERCISE 2:</b> {self.explosive_choice.name} - {choice(self.explosive_choice.reps)}"
        if self.explosive_choice.description: explosive_context += f"\n<i>{self.explosive_choice.description}</i>"
        if self.explosive_choice.link: explosive_context += f"\n{self.explosive_choice.link}"

        # ========================================================================================= 3rd exercise
        if self.additional_choice:
            additional_context = f"<b>ADDITIONAL:</b> {self.additional_choice.name} - {choice(self.additional_choice.reps)}"
            if self.additional_choice.description: additional_context += f"\n<i>{self.additional_choice.description}</i>"
            if self.additional_choice.link: additional_context += f"\n{self.additional_choice.link}"
        else:
            additional_context = "<b>ADDITIONAL:</b> Ø"

        return exercise_context + delimiter + explosive_context + delimiter + additional_context
