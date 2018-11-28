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
typedef vector<bool> vb;
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
    int n, k;
    cin >> n >> k;
    vb x(n + 2);
    rep (i, n + 2) x[i] = false;
    x[0] = true;
    x[n + 1] = true;
    int l = 0, r = n + 1;
    while (k--) {
      vi people;
      for (int i = n + 1; i >= 0; i--) {
        if (x[i]) people.pub(i); 
      }
      
      //rep(i, people.size()) d("people " << people[i] << " ");
      //D("");

      int maxdis = -1;
      rep (i, people.size() - 1) {
        //D(people[i] << " " << people[i + 1]);
        if (maxdis < people[i] - people[i + 1]) {
          maxdis = people[i] - people[i + 1];
          l = people[i + 1];
          r = people[i];
        }
      }
      int mid = (l + r) / 2;
      x[mid] = true;

      //D("l mid r " << l << " " << mid << " " << r);

      if (k == 0) {
        int left = (l + r) / 2 - l - 1;
        int right = r - (l + r) / 2 - 1;
        D("Case #" << p + 1 << ": " << max(left, right) << " " << min(left, right));
      }
    }
  }
  return 0;
}

