import googlerese

def test_decode():
  encoded_phrase = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
  expected = "our language is impossible to understand"
  assert expected == googlerese.decode(encoded_phrase)

  encoded_phrase = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
  expected = "there are twenty six factorial possibilities"
  assert expected == googlerese.decode(encoded_phrase)

  encoded_phrase = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
  expected = "so it is okay if you want to just give up"
  assert expected == googlerese.decode(encoded_phrase)

  encoded_phrase = "y qee"
  expected = "a zoo"
  assert expected == googlerese.decode(encoded_phrase)
