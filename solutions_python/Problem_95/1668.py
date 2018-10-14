alphabet = "abcdefghijklmnopqrstuvwxyz"
chiphertext = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
plaintext = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"

translation = {' ':' ', 'a':'y', 'o':'e', 'z':'q', 'q':'z'}
for i in range(len(chiphertext)):
    translation[chiphertext[i]] = plaintext[i]

T = int(raw_input())
for t in range(1, T+1):
    G = raw_input()
    S = ""
    for g in G:
	S += translation[g]
    print "Case #%d: %s" % (t, S) 
