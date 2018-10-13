def build_mapping(samples):
    mapping = [' ']*(ord('z')-ord('a')+1)
    for (o,t) in samples:
        for i in range(len(o)):
            if t[i] == ' ':
                continue
            mapping[ord(t[i]) - ord('a')] = o[i]

    print mapping
    for i in range(len(mapping)):
        print "%s -> %s" % (chr(ord('a') + i), mapping[i])
        if mapping[i] == ' ':
            raise Exception("could not build mapping")

mapping = build_mapping([("our language is impossible to understand","ejp mysljylc kd kxveddknmc re jsicpdrysi"),
                        ("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"),
                        ("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv"),
                        ("a zoo", "y qee"),
                        ("q", "z")])
