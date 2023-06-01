# Step 1 = fazer o merge sort para conseguir ir quebrando a lista
# = dividir por 2 pegar a esquerda e direita
# Step 2 = proximo metodo 2 listas ordenadas para mesclar em uma unica lista
# utilizar append para acrescentar o elemento no final da lista com
# os if enquanto o tamanho
# do elemento(i, j) for maior ou igual retornar incremento em 1
# https://www.w3schools.com/python/ref_list_append.asp
# Step 3 = colocar as strings em lower case, validar se
# as strings forem vazias retornar false
# Step 4 = se os sort one for igual ao sort two retornar o join,
# o metodo join pega todo os items
# interáveis e junta em uma string
# https://www.w3schools.com/python/ref_string_join.asp
def merge_sort_list(list_string):
    if len(list_string) <= 1:
        return list_string
    mid = len(list_string) // 2
    left = merge_sort_list(list_string[:mid])
    right = merge_sort_list(list_string[mid:])
    return merge(left, right)


def merge(left, right):
    merged_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    while i < len(left):
        merged_list.append(left[i])
        i += 1
    while j < len(right):
        merged_list.append(right[j])
        j += 1
    return merged_list


def is_anagram(first_string, second_string):
    string_one = first_string.lower()
    string_two = second_string.lower()
    if string_one == '' and string_two == '':
        return string_one, string_two, False
    sorted_one = merge_sort_list(string_one)
    sorted_two = merge_sort_list(string_two)
    if sorted_one == sorted_two:
        return ''.join(sorted_one), ''.join(sorted_two), True
    else:
        return ''.join(sorted_one), ''.join(sorted_two), False
