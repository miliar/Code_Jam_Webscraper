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
    // freopen("Jam2017A.inp", "r", stdin);
    // freopen("B-large.in", "r", stdin);
    // freopen("Jam2017B.out", "w", stdout);

    int t;
    cin >> t;

    ll n;
    rep(it, 1, t) {
      cin >> n;

      string s = to_string(n);
      int m = s.length();

      string res;
      rep(k, 1, 30) {
        res = s;
        rep(i, 1, m - 1) {
          if (s[i] < s[i-1]) {
            ll tmp = n / pow(10, m - i) - 1;
            res = to_string(tmp);
            rep(j, 0, m -i - 1)
              res += '9';
            break;
          }
        }
        s = res;
      }
      cout << "Case #" << it << ": " << stoll(res) << endl;
    }

    return 0;
}
