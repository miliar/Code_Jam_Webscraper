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


const int D = 1440;
int cc[D], jj[D];
int dp[721][721][3][2];

int solve(int ca, int ja, int last, int first) {
    int& ans = dp[ca][ja][last][first];
    if (ans != -1) {
        return ans;
    }
    if (ca == D/2 && ja == D/2) {
        return ans = last != first;
    }
    
    int x = ca + ja;
    if (ca == D/2) {
        if (jj[x]) return ans = inf;
        return ans = min(inf, (last == 0) + solve(ca, ja+1, 1, first));
    }
    if (ja == D/2) {
        if (cc[x]) return ans = inf;
        return ans = min(inf,(last == 1) + solve(ca+1, ja, 0, first));
    }
    if (jj[x]) {
        return ans = min(inf, (last == 1) + solve(ca +1, ja, 0, x == 0 ? 0 : first));
    }
    if (cc[x]) {
        return ans = min(inf, (last == 0) + solve(ca, ja+1, 1, x == 0 ? 1 : first));
    }
    
    return ans = min((last == 1) + solve(ca+1, ja, 0, x == 0 ? 0 : first), (last == 0) + solve(ca, ja+1, 1, x == 0 ? 1 : first));

}


int main() {
 
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/inp.txt", "r", stdin);
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/BSmall.txt", "w", stdout);
    int T = SS;
    rep(t, T) {
        rep(i, D) cc[i] = jj[i] = 0;
        int ac = SS, aj = SS;
        rep(i, ac) {
            int x= SS, y = SS;
            fori(j, x, y) cc[j] = 1;
        }
        rep(i, aj) {
            int x = SS, y = SS;
            fori(j, x, y) jj[j] = 1;
        }
        rep(i, 721) rep(j, 721) rep(k, 3) rep(l, 3) dp[i][j][k][l] = -1;
        int ans = solve(0, 0, 2, 2);
        
        printf("Case #%d: %d\n", t+1, ans);
    }
}
