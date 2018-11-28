#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define INF 1e9
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

int main() {
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    string num;
    int l, b = -1, c = 0;
    cin >> num;
    l = num.length();
    FOR(i, 0, l - 1) {
      if (num[i] > num[i + 1]) {
        b = i;
        break;
      }
    }
    cout << "Case #" << tc << ": ";
    if (b == -1) {
      cout << num << endl;
    } else if (num[b] == '1') {
      FOR(i, 0, l - 1) cout << '9';
      cout << endl;
    } else {
      for (int i = b; i > 0; i--) {
        if (num[i] != num[i - 1]) {
          c = i;
          break;
        }
      }
      cout << num.substr(0, c) << (char)(num[b] - 1);
      FOR(i, c + 1, l) cout << '9';
      cout << endl;
    }
  }
}
