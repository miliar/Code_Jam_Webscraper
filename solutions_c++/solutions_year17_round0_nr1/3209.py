#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <queue>
#include <stack>
using namespace std;
typedef long long unsigned int ll;

#define REP(i,n) for(int i=0; i<(int)n; i++)
#define rep(n) REP(i,n)
#define EPS (1e-7)
#define INF 1e9
#define PI (acos(-1))

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        string S;
        int K;
        cin>>S>>K;
        int ii = 0;
        int N = S.size();
        int res = 0;
        while(true) {
            if(ii > N - K) {
                bool ok = true;
                for(int i = ii; i < N; ++i) {
                    if(S[i] == '-') {
                        ok = false;
                        break;
                    }
                }
                if(ok) {
                    cout << "Case #" << tt << ": " << res << endl;
                }
                else {
                    cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
                }
                break;
            }

            // check
            if(S[ii] == '+') {
                ++ii;
            }
            else {
                // flip
                ++res;
                for(int i = ii; i < ii+K; ++i) {
                    S[i] = S[i] == '+' ? '-' : '+';
                }
                ++ii;
            }
        }
    }
    return 0;
}
