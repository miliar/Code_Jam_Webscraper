#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(auto i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

const double pi = 3.1415926535897;

ll r[1000], h[1000], rh[1000];
pair<ll, ll> p[1000];

int main() {
 
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/inp.txt", "r", stdin);
 //   freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/ASmall.txt", "w", stdout);
    int T = SS;
    rep(t, T) {
        int n = SS, k = SS;
        rep(i, n) {
            r[i] = SS;
            h[i] = SS;
            rh[i] = r[i]*h[i];
            p[i] = mp(r[i], h[i]);
        }
        sort(p, p+n);
        reverse(p, p+n);
        double res = -1.0;
        rep(i, n) {
            double ans = pi * p[i].XX * p[i].XX;
            V<double> pro;
            pro.clear();
            fori(j, i+1, n) {
                pro.pb(p[j].XX*p[j].YY);
            }
            if (si(pro) < k-1) {
                break;
            }
            sort(all(pro));
            reverse(all(pro));
            double yo = 0;
            rep(j, k-1) {
                yo += pro[j];
            }
            yo *= 2*pi;
            res = max(res, ans + yo);
        }
        
        printf("Case #%d: %.6lf\n", t+1, res);
    }
}
