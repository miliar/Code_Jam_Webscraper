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

const int MAXK = 32;
int d[MAXK];

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        ll N;cin>>N;
        fill_n(d, MAXK, 0);
        ll ntmp = N;
        int K = 0;
        while(ntmp) {
            d[K++] = ntmp % 10;
            ntmp /= 10;
        }

        // check
        for(int i = K-1; i > 0; --i) {
            if(d[i] <= d[i-1]) {
                continue;
            }

            // not tidy (d[i] >= 1)
            d[i] -= 1;
            for(int j = i-1; j >= 0; --j) {
                d[j] = 9;
            }

            // check upper digit again
            if(i < K-1) {
                i += 2;
            }
        }

        // compose
        ll res = 0;
        for(int i = K-1; i >= 0; --i) {
            res *= 10;
            res += d[i];
        }
        cout << "Case #" << tt << ": " << res << endl;
    }
    return 0;
}
