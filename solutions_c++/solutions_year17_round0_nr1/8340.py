#include <cstdio>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
#include <set>
#include <deque>
#include <utility>
#include <chrono>
#include <sstream>
#include <iomanip>

#define INF 1 << 30
#define MOD 1000000007;
#define PI 3.14159265358979
#define rep(i, n) for (int (i) = 0; (i) < (int)(n); (i)++)
#define reu(i, l, r) for (int (i) = (int)(l); (i) < (int)(r); (i)++)
#define D(x) cout << x << endl
#define d(x) cout << x
#define all(x) (x).begin(), (x).end()
#define pub(x) push_back(x)
#define pob() pop_back()
#define puf(x) push_front(x)
#define pof() pop_front()
#define mp(x, y) make_pair((x), (y))
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<long long> vll;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<long, long> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
template<typename T, typename U> inline void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if (x < y) x = y; }

static const int dx[] = {0, 0, 1, -1};
static const int dy[] = {-1, 1, 0, 0};

int main() { 
  int t;
  cin >> t;
  string s;
  int k;
  rep (p, t) {
    cin >> s >> k;
    int ans = 0;
    int i = 0;
    for (; i < s.size() - k + 1; i++) {

      if (s[i] == '+') continue;

      int cnt = 0;
      while (s[i] == '-' && cnt < k) {
        cnt++;
        i++;
      }

      //D(i << " " << cnt);

      if (cnt == k) {
        ans++;
        i--;
        continue;
      } else if (cnt < k && i + k <= s.size()) {
        ans += 2;
        for (int j = i - cnt + k; j < i + k; j++) {
          s[j] = (s[j] == '+' ? '-' : '+');
        }
      } else {
        ans++;
        i -= cnt;
        for (; i < s.size(); i++) {
          s[i] = (s[i] == '+' ? '-': '+');
        }
        i -= k;
        break;
      }
    }

    bool flag = true;
    while (i < s.size()) {
      if (s[i] == '-') {
        flag = false;
        break;
      }
      i++;
    }

    if (flag) D("Case #" << p + 1 << ": " << ans);
    else D("Case #" << p + 1 << ": " << "IMPOSSIBLE");

  }
  return 0;
}

