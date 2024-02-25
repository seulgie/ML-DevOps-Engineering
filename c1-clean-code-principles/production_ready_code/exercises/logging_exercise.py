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
        logging.info(a, b)
        assert isinstance(a, int)
        assert isinstance(b, int)
        logging.info("SUCCESS: it looks like the values are ints")
        return a + b
    except AssertionError:
        logging.info(a, b)
        logging.error("It appears the a and b are not ints")


if __name__ == "__main__":
    sum_vals("no", "way")
    sum_vals(4, 5)
