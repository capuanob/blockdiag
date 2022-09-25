FROM fuzzers/atheris:2.0.7-python3.9

# Build
WORKDIR /mail-parser
RUN pip install blockdiag

ADD ./mayhem/fuzz_parse_string.py /fuzz_parse_string.py

WORKDIR /
CMD ["/fuzz_parse_string.py"]
