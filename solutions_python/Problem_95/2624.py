replacements = {"#\n":"\n",
                "# ":" ",
                "#a":"y", 
                "#y":"a",
                "#n":"b",
                "#f":"c",
                "#i":"d",
                "#c":"e",
                "#w":"f",
                "#o":"k",
                "#l":"g",
                "#b":"h",
                "#k":"i",
                "#u":"j",
                "#m":"l",
                "#x":"m",
                "#s":"n",
                "#e":"o",
                "#v":"p",
                "#p":"r",
                "#d":"s",
                "#q":"z",
                "#r":"t",
                "#j":"u",
                "#g":"v",                
                "#z":"q",
                "#t":"w",
                "#h":"x"
                }

file = open("A-small-attempt1.in", "r")
mess = file.read()
processed = ""

for x in mess:
    processed += "#" + x

for k, v in replacements.iteritems():
    processed = processed.replace(k,v)

print processed
