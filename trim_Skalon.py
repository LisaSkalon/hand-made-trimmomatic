from Bio.SeqIO.QualityIO import FastqGeneralIterator
import argparse


def parse_inputs():
     parser = argparse.ArgumentParser(description='Trimmomatic')
     parser.add_argument('-i', '--input' , help='Input file' , metavar='Str',
                    type=str, required=True)
     parser.add_argument('-o', '--output' , help='Output file' , metavar='Str',
                    type=str, required=True)
     parser.add_argument('-d', '--head', help = 'Score for headcrop', metavar = 'Int', type = int, default = -5)
     parser.add_argument('-t', '--tail', help = 'Score for tailcrop', metavar = 'Int', type = int, default = -5)

     args = parser.parse_args()
     return args.input, args.output, args.head, args.tail
 
    
if __name__ == '__main__':
    in_file, out_file, head, tail = parse_inputs()
    
    out = open(out_file, "a")
    with open(in_file, "r") as handle:
        
        for (title, seq, qual) in FastqGeneralIterator(handle):
            a = len(seq)
            out.write("%sn" % title)
            out.write('\n')
            out.write("%sn" % (seq[head:(a-tail)]))
            out.write('\n')
            out.write("%sn" % (qual[head:(a-tail)]))
            out.write('\n')
        out.close()