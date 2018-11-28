#include <bits/stdc++.h>
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

int test;
LL D, N, K[1005], S[1005];

int main() {
    cin >> test;
    REP(tt, test) {
        cin >> D >> N;
        REP(i,N) cin >> K[i] >> S[i];
        //cout << "D:" << D << ",N:" << N << endl;

        /*
        double lo = 0, hi = D + 1;
        while (hi - lo > 1e-7) {
            double mid = (lo + hi) / 2;
            //dbg(mid);
            bool can = true;
            REP(i,N) {
                double rem = D - K[i];
                //dbg(rem);
                if (rem / S[i] > mid) {
                    can = false;
                    break;
                }
            }

            if (can) hi = mid;
            else lo = mid;
        }
        */

        double slow = 0;
        REP(i,N) {
            double rem = D - K[i];
            slow = max(slow, rem / S[i]);
        }
        //cout << "Case #" << tt + 1 << ":" << D / (double)mid <
        //printf("Case #%d: %.6lf\n", tt + 1, D / lo);
        cout << "Case #" << tt + 1 << ": " << fixed << setprecision(6) << D / slow << endl;
    }
    return 0;
}
