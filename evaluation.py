import matplotlib.pyplot as plt
import numpy as np


def random_choice_p(
    items, probabilities=None, size=None, factor=3.33, fixed=None, exclude=None
):
    """Pick item based on probabilities and update probabilities."""
    if probabilities is None:
        probabilities = np.ones(len(items)) / len(items)
    items = np.array(items)
    choice_prob = probabilities.copy()

    if type(exclude) == list:
        excluded_indices = [students.index(excluded_item) for excluded_item in exclude]
        for i in excluded_indices:
            choice_prob[i] = 0.0
            choice_prob /= choice_prob.sum()
    elif type(exclude) == str:
        raise ValueError("exclude must be a list or None.")

    if type(fixed) == list:
        if len(list) == size:
            chosen_items = fixed
            chosen_indices = [
                students.index(chosen_item) for chosen_item in chosen_items
            ]
        else:
            raise ValueError("fixed must have the same length as size.")

    else:
        chosen_indices = np.random.choice(
            len(items), size=size, replace=False, p=choice_prob
        )
        chosen_items = items[chosen_indices]
    probabilities[chosen_indices] /= factor

    probabilities /= probabilities.sum()

    return chosen_items, chosen_indices, probabilities


def plot_probs(probabilities, students):
    """Plot the probabilities to be chosen for each student."""

    plt.figure(figsize=(14, 6))
    plt.bar(students, probabilities, width=0.95)
    plt.title("Probabilities for next session", fontsize=17)
    plt.ylabel("probabilites", fontsize=15)
    plt.xlabel("students", fontsize=15)
    plt.xticks(rotation=45, fontsize=15)
    plt.ylim(0, 0.55)
    plt.show()