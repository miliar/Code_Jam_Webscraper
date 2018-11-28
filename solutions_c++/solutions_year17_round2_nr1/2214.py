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

const int MAXN = 1024;
ll K[MAXN];
ll S[MAXN];

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        double res = 0.0;
        ll D,N; cin>>D>>N;
        // cout << D << endl; cout << N << endl;
        fill_n(K, MAXN, 0); fill_n(S, MAXN, 0);
        REP(i,N) { cin>>K[i]; cin>>S[i]; }
        // REP(i,N) { cout << K[i] << endl; }
        // REP(i,N) { cout << S[i] << endl; }
        // --

        double maxh = 0.0;
        REP(i,N) { double h = ((double)(D - K[i])) / S[i]; maxh = max(maxh, h); }
        // cout << maxh << endl;

        // --
        res = D / maxh;

        // --
        cout << "Case #" << tt << ": ";
        printf("%.6f\n", res);
    }
    return 0;
}
