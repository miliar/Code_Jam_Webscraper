// CONTEST SOURCE
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <sstream>
#include <set>
#include <unordered_map>
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
#define inf 1000000000
int t, n, a[4], p, c[4];
int f[101 * 101 * 101 * 101];
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> n >> p;
    for(int i = 0; i < p; ++i) a[i] = 0;
    for(int i = 0; i < n; ++i) {
      int x; cin >> x; a[x % p]++;
    }
    memset(f, 0, sizeof(f));
    for(int cur = 0; ; ++cur) {
      int cop = cur;
      int c[4], rem = 0;
      for(int i = 0; i < p; ++i) {
        c[i] = cop % (a[i] + 1);
        cop /= (a[i] + 1);
        rem += c[i] * i;
      }
      if (rem % p) rem = 0; else rem = 1;
      int mul = 1;
      bool fin = 1;
      for(int i = 0; i < p; ++i) {
        if (c[i] < a[i]) {
          fin = 0;
          if (f[cur + mul] < f[cur] + rem) {
            f[cur + mul] = f[cur] + rem;
          }
        }
        mul *= (a[i] + 1);
      }
      if (fin) {
        cout << "Case #" << tc << ": " << f[cur] << endl;
        break;
      }
    }
  }
}
