#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
bool ISINT(double x){return fabs(x-(int)round(x))<EPS;}
bool ISEQ(double x,double y){return fabs(x-y)<EPS;}
string itos(ll x){stringstream ss;ss<<x;return ss.str();}
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

int main() {
  cin.tie(0);
  ios::sync_with_stdio(0);

  int T;
  cin >> T;

  for (int CASE = 1; CASE <= T; CASE++) {
    cout << "Case #" << CASE << ": ";

    string s;
    int n;
    cin >> s >> n;

    int res = 0;

    for (int i = 0; i + n <= s.size(); i++) {
      if (s[i] == '+') continue;
      res++;
      for (int j = i; j < i + n; j++) {
        s[j] = (s[j] == '+' ? '-' : '+');
      }
    }

    bool possible = true;

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '-') {
        possible = false;
        break;
      }
    }

    if (possible) {
      cout << res << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
