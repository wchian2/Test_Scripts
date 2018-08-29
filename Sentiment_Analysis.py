user1_review = "This was a great item and I find it useful"
user2_review = "Oh my god that was awful. Returned!"
user3_review = "Where do I begin??? It was bad. Not useful at all"

# initialize punctuations... should be removed prior to text analysis
punctuation = ".,!?"

# declare a really small lexicon of vocabularies
very_negative = ["awful", "horrible"]
negative = ["bad", "poor", "crap"]
positive = ["great", "useful", "good"]

def rating_predictor(text):

    # remove punctuations
    text_without_punctuations = ""
    for letter in text:
        if letter not in punctuation:
            text_without_punctuations += letter
        else:
            text_without_punctuations += " "

    # convert all letters to lowercase and split the sentence into a Python list of words
    score = 0
    for word in text_without_punctuations.lower().split():
        if word in very_negative:
            score += -3
        elif word in negative:
            score += -1
        elif word in positive:
            score += 2
        else:
            score += 0

    # scoring system followed by a return of the result
    if score > 0:
        return "Good review"
    elif score < 0:
        return "Bad review"
    else:
        return "Neutral review"

# Test
"""
user1_review = "This was a great item and I find it useful"
user2_review = "Oh my god that was awful. Returned!"
user3_review = "Where do I begin??? It was bad. Not useful at all"
"""

print(rating_predictor(user1_review)) # prints "Good review" ... accurate
print(rating_predictor(user2_review)) # prints "Bad review" ... accurate

print(rating_predictor(user3_review))
# prints "Good review" ... wrong, bad=-1 score, useful=2, total=1...
# but the function does not account for the "not" before the "useful"