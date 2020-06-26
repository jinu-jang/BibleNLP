index_to_book = {
    1: "Matthew",
    2: "Mark",
    3: "Luke",
    4: "John",
    5: "Acts",
    6: "Romans",
    7: "1Corinthians",
    8: "2Corinthians",
    9: "Galatians",
    10: "Ephesians",
    11: "Philippians",
    12: "Colossians",
    13: "1Thessalonians",
    14: "2Thessalonians",
    15: "1Timothy",
    16: "2Timothy",
    17: "Titus",
    18: "Philemon",
    19: "Hebrews",
    20: "James",
    21: "1Peter",
    22: "2Peter",
    23: "1John",
    24: "2John",
    25: "3John",
    26: "Jude",
    27: "Revelation"
}

"""
Takes in either a number between 1 and 27 or a book name.
Reads in the appropriate book and returns a pandas dataframe.
"""
def load_book(book, folder='./new_testament/'):
    import pandas as pd
    
    if book in index_to_book:
        filename = f"{book:02}_{index_to_book[book]}.csv"
    elif book in index_to_book.values():
        book_to_index = dict(zip(index_to_book.values(), index_to_book.keys()))
        filename = f"{book_to_index[book]:02}_{book}.csv"
    else:
        raise ValueError("Unexpected book. Please enter 1~27 or correct name of book")
    return pd.read_csv(folder + filename, delimiter="|")