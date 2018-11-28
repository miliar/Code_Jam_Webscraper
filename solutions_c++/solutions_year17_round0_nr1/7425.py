/* You lost the game. */

#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <fstream>
#include <vector>

#define fin(i,n) for (int i = 0; i < n; i++)
#define fin2(i,a,b) for (int i = a; i < b; i++)

#define mp make_pair
#define mt make_tuple
#define pb push_back
#define mod 1000000007

#define si(n) scanf("%d", &n)
#define sii(n,m) scanf("%d %d", &n, &m)
#define siii(n,m,k) scanf("%d %d %d", &n, &m, &k)
#define sl(n) scanf("%lld", &n)
#define sll(n,m) scanf("%lld %lld", &n, &m)
#define slll(n,m,k) scanf("%lld %lld %lld", &n, &m, &k)
#define sd(n) scanf("%lf", &n)
#define sdd(n,m) scanf("%lf %lf", &n, &m)
#define sddd(n,m,k) scanf("%lf %lf %lf", &n, &m, &k)
#define ss(s) scanf("%s", s)
#define sai(t,n) fin(i,n) { scanf("%d", &t[i]); }
#define sal(t,n) fin(i,n) { scanf("%lld", &t[i]); }
#define sad(t,n) fin(i,n) { scanf("%lf", &t[i]); }

#define pi(n) printf("%d\n", n)
#define pc(n) printf("%c\n", n)
#define ps(s) printf("%s\n", s);
#define pii(n,m) printf("%d %d\n", n, m)
#define pl(n) printf("%lld\n", n)
#define pll(n,m) printf("%lld %lld\n", n, m)
#define pd(n) printf("%lf\n", n)
#define pai(t,n) fin(i,n) { printf("%d ", t[i]); } printf("\n"); 
#define pal(t,n) fin(i,n) { printf("%lld ", t[i]); } printf("\n"); 

#define L long long int
#define D double
#define PII pair<int, int>
#define VPII vector<PII>
#define VL vector<L>
#define VI vector<int>
#define VVI vector<VI>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,k,n,r;
    char org[1111], s[1111];
    si(t);
    fin(i, t) {
        ss(org);
        si(k);
        n = strlen(org);
        r = 0;
        fin(l, n+1) { s[l] = org[l]; }
        int j = 0;
        while (j+k <= n) {
            while (j+k <= n && s[j] == '+') { j++; }
            if (j+k > n) { break; }
            fin2(l, j, j+k) { if (s[l] == '-') { s[l] = '+'; } else { s[l] = '-'; } }
            r++;
        }
        fin2(l, j, n) { if (s[l] == '-') { r = -1; break; } }
        if (r == -1) { printf("Case #%d: IMPOSSIBLE\n", i+1); }
        else { printf("Case #%d: %d\n", i+1, r); }
        
    }
    return 0;
} 