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

typedef pair<ll,ll> pll;
#define HR first
#define R second
vector<pll> v;

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        double res = 0.0;

        // init
        ll N,K; cin>>N>>K;
        v.clear();
        // cout << "v.size: " << v.size() << endl;
        REP(i,N) {
            ll r,h; cin>>r>>h;
            v.push_back(pll(h*r,r));
        }

        // sort by HR
        sort( v.begin(), v.end(), greater<pll>() ); //(100,100),(100,99),(99,*),...
        // REP(i,N) cout << v[i].HR << "," << v[i].R << endl;

        // 0..N-1
        ll rmax = 0.0;
        // cout << "rmax: " << rmax << endl;
        REP(i,K-1) {
            res += 2.0 * PI * (double)v[i].HR;
            rmax = max(rmax, v[i].R);
        }
        // cout << "rmax: " << rmax << endl;
        res += PI * ((double)rmax) * ((double)rmax);

        // N (last)
        double reslastmax = -INF;
        for(int i = K-1; i < (int)N; ++i) {
            double reslast = 0.0;
            if(v[i].R > rmax) {
                reslast = PI * ((double)v[i].R*(double)v[i].R - (double)rmax*(double)rmax);
            }
            reslast += 2.0 * PI * (double)v[i].HR;
            reslastmax = max(reslastmax, reslast);
        }
        res += reslastmax;

        cout << "Case #" << tt << ": ";
        printf("%.9f\n", res);
    }
    return 0;
}
