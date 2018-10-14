in_file = open("A-small-attempt2.in", 'r')
out_file = open("A-small-attempt2.out", 'w')

T = eval(in_file.readline())
for i in range(T):
    N, K = map(eval, in_file.readline().split(" "))
    out_string = "Case #" + str(i+1) + ": " + ("ON" if (K+1) % 2**N == 0 else "OFF") + "\n"
    out_file.write(out_string)
    
in_file.close()
out_file.close()