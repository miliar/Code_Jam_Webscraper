#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>


using namespace std;
int main(int argc, char **argv) {
    int T;
    cin >> T;
    for(int cn=1;cn<=T;++cn) {
        long long NN;
        cin >> NN;
        ++NN;
        char buf[64];
        sprintf(buf, "%lld", NN);
        const int N = strlen(buf);
        long long best = 0;
        long long curr = 0;
        char min_char = '0';
        for(int i=0;i<N;++i) {
            int ndigs = N-i-1;
            for(int c=min_char;c<buf[i];++c) {
                long long cc = curr;
                cc *= 10;
                cc += c-'0';
                for(int nn=0;nn<ndigs;++nn) {
                    cc *= 10;
                    cc += 9;
                }
                best = max(best, cc);
            }
            if(buf[i] < min_char){break;}
            min_char = max(min_char, buf[i]);
            curr *= 10;
            curr += min_char-'0';
        }
        printf("Case #%d: %lld\n", cn, best);
    }
    return 0;
}
