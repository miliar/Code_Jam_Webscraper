// Author: Mahesh
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

//int dis[100][100];
//int DI[100], SP[100];
//int to[100], from[100];
//
//int lin[100];
//
//double dp[100][100];
//
//double solve(int x, int h, int N) {
//    if (x == N-1) {
//        return 0;
//    }
//    double& ans = dp[x][h];
//    if (ans > -1.5) {
//        return ans;
//    }
//    
//    int traveled = lin[x] - lin[h];
//    int onePossible = traveled + dis[x][x+1] <= DI[h];
//    int twoPossible = dis[x][x+1] <= DI[x];
//    if (!onePossible && !twoPossible) {
//        return ans = -1;
//    }
//    double one = 0.0, two = 0.0;
//    if (onePossible) {
//        one = solve(x+1, h, N);
//        onePossible = onePossible && one > -0.5;
//    }
//    if (twoPossible) {
//        two = solve(x+1, x, N);
//        twoPossible = twoPossible && two > -0.5;
//    }
//    if (!onePossible && !twoPossible) {
//        return ans = -1;
//    }
//    if (onePossible && twoPossible) {
//        return ans = min(one + dis[x][x+1]/(1.0*SP[h]), two + dis[x][x+1]/(1.0*SP[x]));
//    }
//    if (onePossible) {
//        return ans = one + dis[x][x+1]/(1.0*SP[h]);
//    }
//    return ans = two + dis[x][x+1]/(1.0*SP[x]);
//}
//
//int main() {
// 
//    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/inp.txt", "r", stdin);
//    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/ASmall.txt", "w", stdout);
//    int T = SS;
//    rep(t, T) {
//        int N = SS, Q = SS;
//        rep(i, N) {
//            DI[i] = SS;
//            SP[i] = SS;
//        }
//        rep(i, N) {
//            rep(j, N) {
//                dis[i][j] = SS;
//            }
//        }
//        lin[0] = 0;
//        fori(i, 1, N) {
//            lin[i] = lin[i-1] + dis[i-1][i];
//        }
//        rep(i, Q) {
//            from[i] = SS;
//            to[i] = SS;
//        }
//        rep(i, 100) rep(j, 100) dp[i][j] = -2.0;
//        double ans = solve(0, 0, N);
//        printf("Case #%d: %.9lf\n", t+1, ans);
//    }
//}
//

int main() {

    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/inp.txt", "r", stdin);
    freopen("/Users/mahesh/Desktop/Codeforces/Codeforces/ASmall.txt", "w", stdout);
    int T = SS;
    rep(t, T) {
        int N = SS, R = SS, O = SS, Y = SS, G = SS, B = SS, VV = SS;
        V<pair<int, char>> v;
        v.pb(mp(R, 'R'));
            v.pb(mp(Y, 'Y'));
            v.pb(mp(B, 'B'));
        sort(all(v));
        if (v[2].XX - v[1].XX > v[0].XX) {
            printf("Case #%d: IMPOSSIBLE\n", t+1);
            continue;
        }
        printf("Case #%d: ", t+1);
        int trips = v[0].XX;
        int doubles = v[1].XX-v[0].XX, singles = v[2].XX-v[1].XX;
        char aa = v[0].YY, bb = v[1].YY, cc = v[2].YY;
        rep(i, singles) {
            printf("%c%c%c%c", aa, cc, bb, cc);
        }
        rep(i, trips - singles) {
            printf("%c%c%c", aa, bb, cc);
        }
        rep(i, doubles) {
            printf("%c%c", bb, cc);
        }
        puts("");
    }
}

