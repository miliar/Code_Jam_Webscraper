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

const int MAXN = 64;
double P[MAXN];

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        // initialize
        int N,K; cin>>N>>K;
        double U; cin>>U;
        fill_n(P, MAXN, 0.0);
        REP(i,N) cin>>P[i];

        // sort
        sort( P, P+N, less<double>() ); //98,99,100,...

        // use U
        while(U > EPS) {
            // cout << "U: " << U << endl;
            double pmin = P[0];
            // cout << "pmin: " << pmin << endl;
            int nmin = 0;
            REP(i,N) if(P[i] - pmin < EPS) ++nmin;
            // cout << "nmin: " << nmin << endl;
            if(nmin == N) {
                REP(i,N) P[i] += U / (double)N;
                U = 0.0;
            }
            else {
                double uu = (P[nmin] - pmin) * nmin;
                if(uu > U) {
                    REP(i,nmin) P[i] += U / (double)nmin;
                    U = 0.0;
                }
                else {
                    REP(i,nmin) P[i] += uu / (double)nmin;
                    U -= uu;
                }
            }
        }
        // REP(i,N) cout << P[i] << endl;

        // print result
        double res = 1.0;
        REP(i,N) res *= P[i];
        cout << "Case #" << tt << ": ";
        printf("%.6f\n", res);
    }
    return 0;
}
