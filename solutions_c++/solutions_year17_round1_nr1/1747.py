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

// This code performs maximum bipartite matching.
//
// Running time: O(|E| |V|) -- often much faster in practice
//
//   INPUT: w[i][j] = edge between row node i and column node j
//   OUTPUT: mr[i] = assignment for row node i, -1 if unassigned
//           mc[j] = assignment for column node j, -1 if unassigned
//           function returns number of matches made
bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < w[i].size(); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}
int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);
  int ct = 0;
  for (int i = 0; i < w.size(); i++) {
    VI seen(w[0].size());
    if (FindMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,r,c;
    char g[50][50];
    si(t);
    fin(k, t) {
        sii(r,c);
        fin(j, r) { ss(g[j]); }
        char d;
        int ok = 1, deb = 0;
            fin(i, r) {
                ok = 0;
                fin(j, c) {
                    if (g[i][j] != '?') {
                        ok = 1;
                        if (j > 0 && g[i][j-1] == '?') {
                            fin(p, j) { g[i][p] = g[i][j]; }
                        }
                        int p = j+1;
                        while (p < c && g[i][p] == '?') { g[i][p] = g[i][j]; }
                    }   
                }
                if (ok == 0) {
                    if (deb == 1) {
                        fin(j, c) { g[i][j] = g[i-1][j]; }
                    }
                }
                else {
                    if (i > 0 && deb == 0) {
                        fin(k, i) {
                            fin(j, c) {
                                g[k][j] = g[i][j];
                            }
                        }
                    }
                    deb = 1;
                }
            }
        printf("Case #%d:\n", k+1);
        fin(i, r) { ps(g[i]); }
    }
    return 0;
} 