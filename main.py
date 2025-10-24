import random

VOWELS = set('aeiou')

def rand_letter():
    return chr(ord('a') + random.randint(0, 25))

def make_word(n=4):
    if n == 0:
        return ''
    return rand_letter() + make_word(n-1)

def make_row(size, cols_left=None):
    if cols_left is None:
        cols_left = size
    if cols_left == 0:
        return []
    return [make_word(4)] + make_row(size, cols_left - 1)

def make_matrix(size, rows_left=None):
    if rows_left is None:
        rows_left = size
    if rows_left == 0:
        return []
    return [make_row(size)] + make_matrix(size, rows_left - 1)

def has_vowel(word, idx=0):
    if idx == len(word):
        return False
    if word[idx] in VOWELS:
        return True
    return has_vowel(word, idx + 1)

def count_vowel_words_dc(matrix, r0, r1, c0, c1):
    if r0 >= r1 or c0 >= c1:
        return 0
    if r1 - r0 == 1 and c1 - c0 == 1:
        return 1 if has_vowel(matrix[r0][c0]) else 0
    rm = (r0 + r1) // 2
    cm = (c0 + c1) // 2
    return (
        count_vowel_words_dc(matrix, r0, rm, c0, cm) +
        count_vowel_words_dc(matrix, r0, rm, cm, c1) +
        count_vowel_words_dc(matrix, rm, r1, c0, cm) +
        count_vowel_words_dc(matrix, rm, r1, cm, c1)
    )

def _print_row(row, idx=0, acc=''):
    if idx == len(row):
        print(acc.rstrip())
        return
    new_acc = acc + row[idx] + (' ' if idx < len(row) - 1 else '')
    _print_row(row, idx + 1, new_acc)

def print_matrix(matrix, row_idx=0):
    if row_idx == len(matrix):
        return
    _print_row(matrix[row_idx])
    print_matrix(matrix, row_idx + 1)

def main():
    try:
        n = int(input('Ingrese el tamaño N de la matriz NxN: '))
    except Exception:
        n = 8
    if n <= 0:
        n = 8

    random.seed() 
    m = make_matrix(n)
    print('Matriz generada:')
    print_matrix(m)
    total = count_vowel_words_dc(m, 0, n, 0, n)
    print(f"\nTotal de palabras con al menos una vocal: {total} de {n*n}")

if __name__ == '__main__':
    main()
