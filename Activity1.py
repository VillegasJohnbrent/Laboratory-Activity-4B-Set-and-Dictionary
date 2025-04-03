# Define the sets based on the Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. How many elements are there in set A and B
# This is the union of A and B
a_union_b = A.union(B)
print(f"a. Number of elements in A ∪ B: {len(a_union_b)}")
# Alternative: len(A | B)

# b. How many elements are there in B that is not part of A and C
# This is B - (A ∪ C)
b_not_in_a_or_c = B.difference(A.union(C))
print(f"b. Number of elements in B - (A ∪ C): {len(b_not_in_a_or_c)}")
# Alternative: len(B - (A | C))

# c. Show the following using set operations
# i. [h, i, j, k]
set_i = C.difference(A)
print(f"i. C - A = {set_i}")
# Alternative: C - A

# ii. [c, d, f]
set_ii = A.intersection(C)
print(f"ii. A ∩ C = {set_ii}")
# Alternative: A & C

# iii. [b, c, h]
set_iii = B.intersection(C.union(A))
print(f"iii. B ∩ (C ∪ A) = {set_iii}")
# Alternative: B & (C | A)

# iv. [d, f]
set_iv = A.intersection(C).difference(B)
print(f"iv. (A ∩ C) - B = {set_iv}")
# Alternative: (A & C) - B

# v. [c]
set_v = A.intersection(B).intersection(C)
print(f"v. A ∩ B ∩ C = {set_v}")
# Alternative: A & B & C

# vi. [l, m, o]
set_vi = B.difference(A.union(C))
print(f"vi. B - (A ∪ C) = {set_vi}")
# Alternative: B - (A | C)