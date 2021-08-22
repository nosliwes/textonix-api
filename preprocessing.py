import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download punkt, wordnet, and stopwords from NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# methods to clean and preprocess text
def preprocess_text(text_list):  
  
  # combine list to single item
  text = ' '.join(text_list)    
  
  # remove special characters
  text = text.replace("\r"," ")
  text = text.replace("\n"," ")
  text = text.replace("\\","/")
  
  # remove punctuation
  punctuation_signs = list("?:!.,;-@#")
  for punct_sign in punctuation_signs:
      text = text.replace(punct_sign, ' ')
      
  # convert to lower case
  text = text.lower()
  
  # lemmitization
  wordnet_lemmatizer = WordNetLemmatizer()
  lemmatized_list = []
  
  # tokenize text
  text_words = text.split(" ")

  # Iterate through word and lemmatize
  for word in text_words:
      lemmatized_list.append(wordnet_lemmatizer.lemmatize(word, pos="v"))
      
  # Join the list and overwrite text
  text = " ".join(lemmatized_list)      

  # Load stop words in english
  stop_words = list(stopwords.words('english'))

  # remove stopwords
  for stop_word in stop_words:
      regex_stopword = r"\b" + stop_word + r"\b"
      text = text.replace(regex_stopword, '')  

  # remove any remaining quotations 
  text = text.replace("'","")
  text = text.replace("\"","")
  
  # trim leading or trailing spaces
  text = text.strip()

  return text

def prepare_message(text_list, tfidf):

  text = preprocess_text(text_list)
  
  # vectorize text
  features = tfidf.transform([text]).toarray()
  
  return features