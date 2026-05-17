import nltk
from nltk.tokenize import word_tokenize

texto = "A disciplina do professor WESLESON é muito boa." 

tokens = word_tokenize(texto)

print("=== TOKENIZAÇÃO ===")
print("\nTexto original:")
print(texto)

print("\nTokens encontrados:")
print(tokens)