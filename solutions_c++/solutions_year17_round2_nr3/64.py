// CONTEST SOURCE
#include <iostream>
#include <sstream>
#include <set>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
//#include <priority_queue>
using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define VI vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair
#define ull unsigned ll
#define inf 1000000000
int t, n, q;
int e[111], s[111];
ll d[111][111];
double l[111][111];
int main() {
  freopen("C-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    scanf("%d%d", &n, &q);
    for(int i = 0; i < n; ++i) scanf("%d%d", &e[i], &s[i]);
    for(int i = 0; i < n; ++i) for(int j = 0; j < n; ++j) {
      int x; scanf("%d", &x); d[i][j] = x;
    }

    for(int i = 0; i < n; ++i) { d[i][i] = 0; }

    for(int k = 0; k < n; ++k) {
      for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
          if (d[i][k] != -1 && d[k][j] != -1) {
            if (d[i][j] == -1) {
              d[i][j] = d[i][k] + d[k][j];
            } else {
              d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
          }
        }
      }
    }

    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) { l[i][j] = 1e100; }
      l[i][i] = 0;
    }

    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) {
        if (d[i][j] != -1 && d[i][j] <= e[i]) {
          l[i][j] = min(l[i][j], d[i][j] * 1. / s[i]);
        }
      }
    }


    for(int k = 0; k < n; ++k) {
      for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
          l[i][j] = min(l[i][j], l[i][k] + l[k][j]);
        }
      }
    }

    printf("Case #%d:", tc);
    while(q--) {
      int st, fn; scanf("%d%d", &st, &fn);
      --st; --fn;
      printf(" %0.15lf", l[st][fn]);
    }
    printf("\n");
  }
}
