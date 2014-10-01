''' Read and print an integer series.'''

import sys

#def read_series(filename):
#    try:
#        f = open(filename, mode='rt', encoding='utf-8')
#        return [int(line.strip()) for line in f]
#        #series = []
#        #for line in f:
#        #    a = int(line.strip())
#        #    series.append(a)
#    finally:
#        f.close()
#    return series

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])