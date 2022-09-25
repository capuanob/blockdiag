#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from blockdiag.parser import parse_string, ParseException, Diagram


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    parse_str = fdp.ConsumeUnicode(atheris.ALL_REMAINING)

    try:
        tree = parse_string(parse_str)
        if not isinstance(tree, Diagram):
            raise RuntimeError("Diagram object not returned")
    except ParseException:
        return


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
