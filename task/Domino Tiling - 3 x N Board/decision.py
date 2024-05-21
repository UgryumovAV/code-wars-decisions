import sys


def three_by_n(n):
    
    return n + 1


if __name__ == "__main__":
    sample_inputs = [
        (2, 3), (4, 11), (10, 571), (20, 413403), (10000, 12003229),
        (1, 2), (3, 18), (5, 106), (11, 11542), (21, 3287999), (9999, 6311027)
    ]
    for wight, answer in sample_inputs:
        assert three_by_n(wight) == answer
        sys.stdout.write("three_by_n({}) = {}".format(wight, answer))
