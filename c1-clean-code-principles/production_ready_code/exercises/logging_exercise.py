import logging

logging.basicConfig(
    filename="./results.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def sum_vals(a, b):
    """
    Args:
      a: (int)
      b: (int)
    Return:
      a + b (int)
    """
    try:
        check_val = a + 1
        print("first number plus one equals {}".format(check_val))
        logging.info("SUCCESS: it looks like the values are ints or floats")
        return a + b
    except TypeError:
        logging.error("It appears the first value is not of type int or float")


if __name__ == "__main__":
    sum_vals("no", "way")
    sum_vals(4, 5)
