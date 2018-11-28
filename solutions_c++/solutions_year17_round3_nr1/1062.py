// Made By Haireden Aibyn
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define fname ""
#define INF 2147483647
#define MOD 1000000007
#define mp make_pair
#define F first
#define S second
#define sc scanf
#define all(x) x.begin(), x.end()
#define size(x) int(x.size())
#define pr printf
#define deb(x) cerr << " | " << #x << " = " << x
#define pb push_back
#define ex exit(0)
#define y1 y4

typedef long long ll;
typedef unsigned long long ull;

const int N = 1111;

int p[N][N];
double d[N][N];
pair <double, double> a[N];

double get(int pos1, int pos2) {
       double sum = a[pos1].F * a[pos1].F + a[pos1].F * a[pos1].S * 2.0;
       if (pos2 == 0) return sum;
       return a[pos1].F * a[pos1].S * 2.0;
}

int main() {
    srand(time(NULL));
    /*#ifndef ONLINE_JUDGE
    freopen(fname".in", "r", stdin);
    freopen(fname".out", "w", stdout);
    #endif       */
    int test;
    cin >> test;
    for (int tt = 1; tt <= test; tt++) {
          int n, k;
          cin >> n >> k;    
          for (int i = 1; i <= n; i++) {
              cin >> a[i].F >> a[i].S;
          }
          sort(a + 1, a + 1 + n);
          reverse(a + 1, a + 1 + n);
          double ans = 0;
          d[0][0] = 0;
          for (int i = 1; i <= k; i++) {
              d[0][i] = -1e18;          
          }
          for (int i = 1; i <= n; i++)
              for (int j = 0; j <= k; j++)
                  p[i][j] = 0;
          for (int i = 1; i <= n; i++) {
              for (int j = 1; j <= k; j++) {
                  d[i][j] = d[i - 1][j];
                  p[i][j] = p[i - 1][j];
                  if (d[i - 1][j - 1] + get(i, p[i - 1][j - 1]) > d[i][j]) {
                     d[i][j] = d[i - 1][j - 1] + get(i, p[i - 1][j - 1]);
                     p[i][j] = i;                  
                  }
              }
          }
          for (int i = 1; i <= n; i++) {
              ans = max(ans, d[i][k]);          
          }
          cout << "Case #" << tt << ": ";
          cout << fixed << setprecision(6) << ans * acos(-1) << endl;    
    }
    return 0;
}