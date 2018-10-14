from __future__ import print_function
import os
import sys
import time
import traceback
from optparse import OptionParser
try:
    import cPickle as pickle
except ImportError:
    import pickle

class attrdict(dict):
    "A dict whose items can also be accessed as member variables."
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        for k,v in self.iteritems():
            if type(v) == type({}):
                self[k] = attrdict(v)
    def __getattr__(self, name):
        return self[name]
    def __setattr__(self, name, val):
        self[name] = val

cj = attrdict()

def chext(file, ext):
    "Returns the given filename with the extension changed"
    if file == "-": return file     # don't change "-", it is used for stdin/stdout
    d = os.path.dirname(file)       # separate into directory
    b = os.path.basename(file)      # ... and basename
    try:
        i = b.rindex(".")           # find last dot in filename
        b = b[:i]                   # and remove from that point on
    except ValueError:
        pass                        # if there is no dot, nothing to remove
    return os.path.join(d, b + ext) # put everything back together

def main(func):
    """Decorator to make a function the codejam main function:
    - automatically run at startup
    - parse command line arguments
    - open input/output data files
    - run function
    - measure elapsed time
    - compare output with answer file if there is one
    """
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-i", "--infile", dest="infilename",
                      help="read data from FILE", metavar="FILE")
    parser.add_option("-o", "--outfile", dest="outfilename",
                      help="write data to FILE", metavar="FILE")
    parser.add_option("-a", "--ansfile", dest="ansfilename",
                      help="answer file to compare to output", metavar="FILE")
    parser.add_option("-v", "--verbose", dest="verbose",
                      help="Print output to terminal as well as file",  action="store_true")
    parser.add_option("-d", "--debug", dest="debug",
                      help="Enable debug output",  action="store_true")
    try:
        (options, args) = parser.parse_args()
        cj.update(options.__dict__)
        if cj.infilename is None:
            cj.infilename = args[0]
        if cj.infilename == "-":
            cj.infile = sys.stdin
        else:
            cj.infile = open(cj.infilename, 'rU')
        if cj.outfilename is None:
            cj.outfilename = chext(cj.infilename, '.out')
        if cj.outfilename == "-":
            cj.outfile = sys.stdout
        else:
            cj.outfile = open(cj.outfilename, 'w')
        if cj.ansfilename is None:
            cj.ansfilename = chext(cj.infilename, '.ans')
        start = time.time()
        result = func() # run function, or init class
        try:
            result = result.run() # if it has a run method, call it
        except AttributeError:
            pass
        stop = time.time()
        print("Time: %.3g s" % (stop-start))
        if cj.infile != sys.stdin: cj.infile.close()
        if cj.outfile != sys.stdout: cj.outfile.close()
        if cj.outfile != sys.stdout and os.path.isfile(cj.ansfilename):
            cmd = "diff '" + cj.ansfilename + "' '" + cj.outfilename + "'"
            print(cmd)
            diff = os.system(cmd)
            print("result:", diff)
        sys.exit(result)
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(1)
    except Exception as e:
        print("ERROR:", e)
        traceback.print_exc()
    parser.print_help()
    sys.exit(2)

def read_str():
    "read a line and return it as a string"
    return cj.infile.readline().rstrip('\n')

def read_strs():
    "read a line and split it into words at spaces, return list of strings"
    return read_str().split(' ')

def read_int():
    "read a line and return it as an integer"
    return int(read_str())

def read_ints():
    "read a line and split it into numbers at spaces, return list of integers"
    return [int(s) for s in read_strs()]

def printcase(case, *args, **kwargs):
    "Output result for one test case, fixing up case to be 1-based"
    "Also output to stdout if verbose is enabled and outfile is not already stdout"
    print("Case #" + str(case+1) + ":", *args, file=cj.outfile, **kwargs)
    if cj.verbose and cj.outfile != sys.stdout:
        print("Case #" + str(case+1) + ":", *args, **kwargs)

def info(*args, **kwargs):
    "Print something only if debug output is enabled"
    if cj.debug:
        print(*args, **kwargs)

def debug(*args, **kwargs):
    "Display values of variables (and kwarg names if present) if debug is enabled"
    if cj.debug:
        for v in args:
            print("DEBUG:", repr(v))
        for k,v in kwargs.iteritems():
            print("DEBUG:", k, "=", repr(v))

class memoized(object):
    """Decorator to memoize a function
    usage:
    @memoized
    def func(a, b):
        pass
    @memoized(argmap=memoized.fixupkw)
    def func(a, b):
        pass
    """
    def __init__(self, func = None, argmap = None, cache = None):
        if argmap == None: argmap = self.simple
        if memoized.function_params(argmap) >= 2:
            self.argmap = argmap
        else:
            self.argmap = lambda x, y: argmap(x)
        if cache == None: cache = dict()
        self.cache = cache
        if func != None:
            if not hasattr(func, "__call__"): raise TypeError("func is not callable")
            self.do_call = self.do_call(func)
    def __call__(self, *args, **kwargs):
        return self.do_call(*args)
    def do_call(self, func):
        def wrapped_func(*args, **kwargs):
            key = self.argmap(args, kwargs)
            try:
                value = self.cache[key]
            except KeyError:
                value = self.cache[key] = func(*args, **kwargs)
            #except TypeError:
            #    value = f(*args, **kwargs)
            return value
        wrapped_func.__name__ = func.__name__
        wrapped_func.__doc__ = func.__doc__
        #wrapped_func._func = func
        #wrapped_func._cache = self.cache
        #wrapped_func._argmap = argmap
        return wrapped_func
    @staticmethod
    def simple(args, kwargs):
        """Returns args unchanged, ignores kwargs.
        All args must be hashable."""
        return args
    @staticmethod
    def simplekw(args, kwargs):
        """Returns args and kwargs unchanged.
        All args must be hashable."""
        return (args, tuple(sorted(kwargs.iteritems())))
        #return (args, frozendict(kwargs.iteritems()))
    @staticmethod
    def fixup(args):
        """Converts all lists to tuples and dicts to frozendicts, ignores kwargs.
        Should work with most args, and be faster than pickle."""
        return tuple(memoized._fixarg(a) for a in args)
    def fixupkw(args, kwargs):
        """Converts all lists to tuples and dicts to frozendicts, in args and kwargs.
        Should work with most args, and be faster than pickle."""
        return (fixup(args), tuple((k,memoized._fixarg(v)) for k,v in sorted(kwargs.iteritems())))
    @staticmethod
    def withpickle(args, kwargs):
        """Pickles args and kwargs.
        Should work with all types."""
        return pickle.dumps((args, kwargs))
    @staticmethod
    def _fixarg(a):
        """Fixes up 'a' to (hopefully) make it hashable"""
        if isinstance(a, list): return tuple(a)
        if isinstance(a, dict): return tuple(sorted(a.iteritems()))
        if isinstance(a, set): return frozenset(a)
        return a
    @staticmethod
    def function_params(f):
        "Returns number of parameters expected by 'f'"
        while not hasattr(f, "func_code"): f = f.__call__
        return f.func_code.co_argcount
