#!/usr/bin/env python
"""
tongue.py

a script for the Google code jam 2012 Qulification Round Problem A

USAGE: python tongue.py filename.in filename.out
"""
import sys

# the maping dicts
GOOGLERESE_TO_ENGLISH = {}
ENGLISH_TO_GOOGLERESE = {}

# what we know about the language
SAMPLES = {
'our language is impossible to understand' : 'ejp mysljylc kd kxveddknmc re jsicpdrysi',
'there are twenty six factorial possibilities' : 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'so it is okay if you want to just give up' : 'de kr kd eoya kw aej tysr re ujdr lkgc jv',
'a zoo' : 'y qee'
}

def set_up_mapping_dicts():
    """
    parses the knowledge we have about GOOGLERESE and fills the two dictionaries
    can automatically map one missing combination. if there are more, you must provide
    more SAMPLE data...
    """
    for key, value in SAMPLES.iteritems():
        i = 0
        while i < len(key):
            ENGLISH_TO_GOOGLERESE[key[i]] = value[i]
            GOOGLERESE_TO_ENGLISH[value[i]] = key[i]
            i += 1
    
    # check whether we have a mapping for every char (=27, because the space is included)
    if len(GOOGLERESE_TO_ENGLISH) < 27:
        missing_in_goog = []
        missing_in_en = []
        missing_in_goog = find_missing_key(GOOGLERESE_TO_ENGLISH)
        missing_in_en = find_missing_key(ENGLISH_TO_GOOGLERESE)
        if(len(missing_in_goog) == 1):
            # fortunately we can map the missing keys
            GOOGLERESE_TO_ENGLISH[missing_in_goog[0]] = missing_in_en[0]
            ENGLISH_TO_GOOGLERESE[missing_in_en[0]] = missing_in_goog[0] 
        else:
            raise Exception("not possible! please provide more sample data")

def find_missing_key(to_check):
    """
    helper function for finding all missing mappsing in a dict
    """
    missing = []
    # check all characters using the ascii table
    for a in range(97, 123):
        if chr(a) not in to_check:
            missing.append(chr(a))
    return missing

def translate_file_to_en(f):
    """
    translates the given (and opened) file to english
    """
    translated = []
    
    # the first line indicates the number of cases
    cases = int(f.readline())
    
    # translate every caes
    for c in range(1, cases + 1):
        googlerese = f.readline()
        translated.append(to_en(c, googlerese))
    
    return translated


def to_en(case, googlerese):
    """
    translates one line to en and prefixes the Case #... identifier
    """
    return translate(case, googlerese, GOOGLERESE_TO_ENGLISH)

def translate(case, line, mapping_dict):
    """
    translates the given line using the given mapping_dict
    """
    translated = []
    
    for l in line:
        if l <> '\n':
            translated.append(mapping_dict[l])
    
    return 'Case #%i: %s\n' % (case, ''.join(translated))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'USAGE: python tongue.py filename.in filename.out'
        sys.exit(0)

    # set up our mapping
    set_up_mapping_dicts()
    
    # translate the lines
    translated = []
    inputfile = file(sys.argv[1], 'r')
    translated = translate_file_to_en(inputfile)
    inputfile.close()

    # write lines to outfile
    out = file(sys.argv[2], 'w')
    out.writelines(translated)
    out.close()
