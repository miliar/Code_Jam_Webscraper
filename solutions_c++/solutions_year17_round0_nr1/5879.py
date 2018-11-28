#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<int> vi;

#define rep(i,a,b) for (int i = a; i <= b; i++)
#define drep(i,a,b) for (int i = a; i >= b; i--)
#define mp(x,y) make_pair((int)x,(int)y)
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define bug(x) {cout << #x << " = " << x << endl;}
#define pa(x,a,b) {cout << #x << " = "; rep(i,a,b) cout << x[i] << ' '; cout << endl;}
#define sz(a) int((a).size())
#define pb push_back
#define ll long long
#define debug 0

using namespace std;

int main() {
    // freopen("A-large.in", "r", stdin);
    // freopen("Jam2017A.out", "w", stdout);

    int t;
    cin >> t;

    string s;
    int k;
    rep(it, 1, t) {
      cin >> s >> k;

      int n = s.length();
      int res = 0;
      rep(i, 0, n - k) {
        if (s[i] == '-') {
          res++;
          rep(j, i, i + k - 1)
            if (s[j] == '-')
              s[j] = '+';
            else
              s[j] = '-';
        }
      }

      rep(i, n - k + 1, n - 1)
        if (s[i] == '-') {
          res = -1;
          break;
        }

      if (res == -1)
        cout << "Case #" << it << ": IMPOSSIBLE" << endl;
      else
        cout << "Case #" << it << ": " << res << endl;
    }

    return 0;
}
