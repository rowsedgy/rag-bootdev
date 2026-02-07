from .search_utils import DEFAULT_SEARCH_LIMIT, load_stop_words, load_movies
from nltk.stem import PorterStemmer
import string

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for movie in movies:
        tokenized_query = tokenize_text(query)
        tokenized_title = tokenize_text(movie['title'])
        
        if has_matching_token(tokenized_query, tokenized_title):
            results.append(movie)
            if len(results) >= limit:
                break       
    return results


def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for q_token in query_tokens:
        for t_token in title_tokens:
            if q_token in t_token:
                return True
    return False


def preprocess_text(text: str) -> list[str]:
    translator = str.maketrans('', '', string.punctuation)
    
    text = text.lower()
    text = text.translate(translator)

    return text

def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split()
    valid_tokens = []
    for token in tokens:
        if token:
            valid_tokens.append(token)
    stop_words = load_stop_words()
    filtered_words = []
    for word in valid_tokens:
        if word not in stop_words:
            filtered_words.append(word)
    stemmed_tokens = stem_tokens(filtered_words)
    return stemmed_tokens


def stem_tokens(tokens: list[str]) -> list[str]:
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens