import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=True, help='Specify the input file path')
    return parser.parse_args()

def prepare(path):
    f = open(path)
    f_content = f.readlines()
    L=[]
    R=[]
    for line in f_content:
        spl = line.split()
        L.append(int(spl[0]))
        R.append(int(spl[1]))
    R.sort()
    L.sort()
    return R, L

def part1(path):
    R,L = prepare(path)
    distances = []
    for i in range(1000):
        distances.append(abs(R[i]-L[i]))
    print(sum(distances))

def part2(path):
    R,L = prepare(path)
    result = []
    for i in range(1000):
        cnt = R.count(L[i])
        result.append(L[i]*cnt)
    print(sum(result))

file_path = parse_args().input_file
part1(file_path)
part2(file_path)






