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
  rep (p, t) {

    unsigned long long n;
    cin >> n;

    int a[20] = { 0 };
    int i = 0;
    while (n > 0) {
      a[i] = n % 10;
      n /= 10;
      i++;
    }

    int b[20];
    rep (j, i) {
      b[i - j - 1] = a[j];
    }

    //rep(j, i) d(b[j]);
    //D("");
    //rep(j, i) D(a[j]);
   
    int cnt = 1;
    int sig = -1;
    int ok = true;
    rep (j, i - 1) {
      if (b[j] < b[j + 1]) {
        cnt = 1;
        continue;
      } else if (b[j] == b[j + 1]) {
        cnt++;
      } else {
        ok = false;
        sig = j;
        break;
      }
    }

    //D(cnt << " " << sig);

    if (!ok) {
      b[sig - cnt + 1]--;
      reu(j, sig - cnt + 2, i) {
        b[j] = 9;
      }
    }

    //rep(j, i) d(b[j]);
    //D("");
    
    unsigned long long ans = 0;

    rep(j, i) {
      ans += b[j];
      if (j != i - 1) ans *= 10;
    }


    D("Case #" << p + 1 << ": " << ans);

  }
  return 0;
}

