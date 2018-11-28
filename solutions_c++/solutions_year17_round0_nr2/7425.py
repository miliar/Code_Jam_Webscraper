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
    int t,n,e,f,ind;
    char s[1111];
    si(t);
    fin(i, t) {
        ss(s);
        n = strlen(s);
        ind = -1;
        fin2(j, 1, n) { 
            e = s[j] - '0';
            f = s[j-1] - '0';
            if (e < f) { ind = j-1; break; }
        }  
        if (ind == -1) { printf("Case #%d: %s\n", (i+1), s);  continue; }
        while (ind > 0 && s[ind] == '0') { ind--; }
        if (ind == 0 && (s[ind] - '0') <= 1) {
            fin(j, n-1) { s[j] = '9'; } 
            s[n-1] = 0;
        } 
        else {
            int val = s[ind];
            while (ind >= 0 && s[ind] == val) { s[ind]--; ind--; }
            ind++;
            fin2(j, ind+1, n) { s[j] = '9'; }
        }
        printf("Case #%d: %s\n", (i+1), s); 
    }
    return 0;
} 