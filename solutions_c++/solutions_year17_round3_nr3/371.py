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



double p[50];

int main() {
 
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/inp.txt", "r", stdin);
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/ASmall.txt", "w", stdout);
    int T = SS;
    rep(t, T) {
        int n = SS, k = SS;
        double ex;
        cin>>ex;
        rep(i, n) cin>>p[i];
        sort(p, p+n);
        int i = 0;
        while (ex > 1e-9) {
            if (i == n-1) {
                rep(j, n) {
                    p[j] += ex / n;
                }
                break;
            }
            double jump = p[i+1]-p[i];
            double need = jump * (i+1);
            double willGive = min(ex, need);
            rep(j, i+1) {
                p[j] += willGive/(i+1);
            }
            ex -= willGive;
            i++;
        }
        double ans = 1;
        rep(i, n) ans*=p[i];
        printf("Case #%d: %.6lf\n", t+1, ans);
    }
}
