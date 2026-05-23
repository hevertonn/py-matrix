import os
import sys

import numpy as np
from PIL import Image


def get_image_path():
    argv = sys.argv

    if len(argv) > 1:
        return argv[1]

    print("The image path must be provided as a parameter!")
    sys.exit()


def create_matrix(image_path):
    if not os.path.exists(image_path):
        print("Image not found!")
        sys.exit()

    if not image_path.endswith(".pbm"):
        print("Invalid format; the image must be in PBM format!")
        sys.exit()

    img = Image.open(image_path)

    return 1 - np.asarray(img, dtype=np.uint8)


def transpose_matrix(matrix):
    transposed_matrix = np.empty((matrix.shape[1], matrix.shape[0]), np.uint8)

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            transposed_matrix[j][i] = element

    return transposed_matrix


def reverse_row_order(matrix):
    reversed_rows_matrix = np.empty(matrix.shape, dtype=np.uint8)

    for i, row in enumerate(matrix):
        reversed_rows_matrix[(matrix.shape[0] - 1) - i] = row

    return reversed_rows_matrix


def reverse_column_order(matrix):
    reversed_columns_matrix = np.empty(matrix.shape, dtype=np.uint8)

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            reversed_columns_matrix[i][(matrix.shape[1] - 1) - j] = element

    return reversed_columns_matrix


def reverse_row_and_column_order(matrix):
    return reverse_column_order(reverse_row_order(matrix))


def save_image(matrix, image_path):
    if not os.path.exists("output"):
        os.mkdir("output")

    matrix = matrix.astype(str)
    image_file = open(f"output/{image_path}", "w")

    image_file.write(f"P1\n{matrix.shape[1]} {matrix.shape[0]}\n")
    for row in matrix:
        image_file.write("".join(row) + "\n")


image_path = get_image_path()
image_matrix = create_matrix(image_path)
print("Matrix created!")

transposed_image_matrix = transpose_matrix(image_matrix)

save_image(reverse_row_order(transposed_image_matrix), "img_1.pbm")
save_image(reverse_column_order(transposed_image_matrix), "img_2.pbm")
save_image(reverse_row_order(image_matrix), "img_3.pbm")
save_image(reverse_row_and_column_order(image_matrix), "img_4.pbm")
save_image(reverse_column_order(image_matrix), "img_5.pbm")
save_image(transposed_image_matrix, "img_6.pbm")
save_image(image_matrix, "img_7.pbm")
save_image(reverse_row_and_column_order(transposed_image_matrix), "img_8.pbm")

print("Images saved in the output folder!")
