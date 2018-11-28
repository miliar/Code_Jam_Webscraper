#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>

using namespace std;

#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define rep(i,a)      for(int i=0;i<a;i++)
#define rep2(i,a,b)      for(int i=a;i<b;i++)
using namespace std;
int test = 1;
void solve() {
  cout << "Case #" << test++ << ": ";
  int d, n;
  cin >> d >> n;
  int k[1000], s[1000];
  rep (i, n) {
    cin >> k[i] >> s[i];
  }
  
  double time = 0;
  rep (i, n) {
    double delta = d - k[i];
    double speed = s[i];
    double timex = delta / speed;
    if (time < timex)
      time = timex;
  }
  double res= (d / time);
  cout << fixed << setprecision(6) << res << endl;
}

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
