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
#include <set>
#include <climits>
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
int t;
string s;
int main() {
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> s;
    bool good = 1;
    for(int i = 0; i < L(s) - 1; ++i) {
      if (s[i] > s[i + 1]) { good = 0; break; }
    }
    if (good) {
        cout << "Case #" << tc << ": " << s << endl;
        continue;
    }
    for(int pos = L(s) - 1; pos >= 0; --pos) {
      if (s[pos] == '0') continue;
      string t = s; --t[pos];
      bool ok = 1;
      for(int i = 0; i < pos; ++i) {
        if (t[i] > t[i + 1]) { ok = 0; break; }
      }
      if (ok) {
        for(int i = pos + 1; i < L(s); ++i) {
          t[i] = '9';
        }
        if (t[0] == '0') t = t.substr(1, L(t) - 1);
        cout << "Case #" << tc << ": " << t << endl;
        break;
      }
    }
  }
}
