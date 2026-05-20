'''
This program prints stdin to the screen.
'''
import sys

CHUNK_SIZE = 64 * 1024


def cat(file):
    output = sys.stdout.buffer
    while data := file.read(CHUNK_SIZE):
        output.write(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
