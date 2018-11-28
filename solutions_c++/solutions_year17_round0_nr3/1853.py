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
int t;
ll n, k;
map<ll, ll> input;
int main() {
  freopen("C-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> n >> k;
    input.clear();
    input[n] = 1;
    while(true) {
      map<ll, ll>::iterator it = input.end(); --it;
      ll maxlen = it->x;
      ll maxcnt = it->y;
      input.erase(it);
      input[maxlen / 2] += maxcnt;
      input[(maxlen - 1)  / 2] += maxcnt;
      k -= maxcnt;
      if (k <= 0) {
        cout << "Case #" << tc << ": " << maxlen / 2 << " " << (maxlen - 1) / 2 << endl;
        break;
      }
    }
  }
}
