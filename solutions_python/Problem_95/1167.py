import string
import sys

fromlist = "abcdefghijklmnopqrstuvwxyz"
tolist = "yhesocvxduiglbkrztnwjpfmaq"
transtable = string.maketrans(fromlist, tolist)


def translate(cyphertext):
    return string.translate(cyphertext, transtable)


def format_output(number, text):
    return "Case #%d: %s\n" % (number, text)


def translate_from_file_to_file(infile, outfile):
    fp_in = open(infile, "r")
    fp_out = open(outfile, "w")
    number_of_lines = int(fp_in.readline().strip())
    for index in xrange(1, number_of_lines + 1):
        line = fp_in.readline().strip()
        fp_out.write(format_output(index, translate(line)))
    fp_in.close()
    fp_out.close()

# python speaking_in_tongues.py input_speaking_in_tongues.txt my_output_speaking_in_tongues.txt
if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    translate_from_file_to_file(infile, outfile)
