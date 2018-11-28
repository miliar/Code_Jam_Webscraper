/* Author: Mahesh */

/* 1. Did u interpret the qns correctly ?
 2. Is your i/o correct ?
 3. Int overflow, double precesion
 4. Array size correct ?
 5. Clearing/resetting vector, map etc.
 6. Stack ovrflow
 7. Global/local conflict
 8. Check for obvious typo(most imp)
 9. Think about edge cases
 */

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
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
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
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

/* Program Body starts here */


int g[10000];

int main() {
    int T = SS;
    rep(t, T) {

    int N = SS, P = SS;
    int g[N];
    rep(i, N) g[i] = SS;
            int yo = 0, res = 0, c1, c2, c3;
            rep(i, N) {
                g[i] %= P;
                if (g[i] == 0)
                    ++yo;
            }
            N -= yo;
            
            int kk = 0;
            if (P == 2) {
                int c = 0;
                iter(x, g) {
                    if (x == 1) {
                        ++c;
                    }
                }
                kk = c;
                res += c / 2;
            } else if (P == 3) {
                int c1 = 0, c2 = 0;
                iter(x, g) {
                    if (x == 1) c1++;
                    else if (x == 2) c2++;
                }
                int r = min(c1, c2);
            } else {
                int m[4];
                iter(x, g) m[x]++;
                int r = min(m[1], m[2]);
                m[1] -= r;
                m[3] -= r;
                res += r;
            }
            
            N-= kk;
            if (N > 0) res++;
        printf("Case #%d: %d\n", res);
    }

}

