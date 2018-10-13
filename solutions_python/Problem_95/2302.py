#!/usr/bin/env python
import sys

def GetMap():
  """Get the translation map using the given sample cases"""

  # This way of mapping automatically ensures that spaces are mapped to spaces
  tongue_speak = """y qee ejp mysljylc kd kxveddknmc re jsicpdrysi
  rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
  de kr kd eoya kw aej tysr re ujdr lkgc jv z"""

  answer = """a zoo our language is impossible to understand
  there are twenty six factorial possibilities
  so it is okay if you want to just give up q"""

  m = {}
  for (t, a) in zip( tongue_speak, answer ):
    # We assert in the following line purely
    # to make sure there is nothing wrong with our code
    # If we have seen t before it must be already
    # mapped to a and nothing else.
    if m.has_key(t): assert m[ t ] == a
    m[ t ] = a

  return m

def TranslateLine( s, translation_map ):
  """Translate a line in the blah speak to normal english."""
  return( "".join( [ translation_map[ c ] for c in s ] ) )

def Main():
  case_number = 1
  translation_map = GetMap()

  sys.stdin.readline() # Discard the first line. We cool pythoners dont need it.
  for line in sys.stdin:
    translated_line = TranslateLine( line.strip(), translation_map )
    print "Case #%d: %s"%( case_number, translated_line )
    case_number += 1
  return


Main()
