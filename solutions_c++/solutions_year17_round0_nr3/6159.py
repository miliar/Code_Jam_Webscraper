#include <iostream>
#include <queue>

using namespace std;
typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef pair<int, int> PII;

#define FOR(i, a, n) for (ll i = (ll)a; i < (ll)n; ++i)
#define REP(i, n) FOR(i, 0, n)
#define ALL(x) x.begin(), x.end()
#define MP make_pair
#define PB push_back
#define MOD 1000000007
#define INF (1LL<<30)
#define LLINF (1LL<<60)
#define PI 3.14159265359
#define EPS 1e-12
#define int ll

int n[105], k[105];
signed main(void)
{
  int t;
  cin >> t;
  REP(i, t) cin >> n[i] >> k[i];

  priority_queue<int> que;
  REP(i, t) {
    while(que.size()) que.pop();
    que.push(n[i]);
    int a, b;
    REP(j, k[i]) {
      int p = que.top();
      que.pop();
      a = (p-1)/2, b = (p-1)-a;
      //cout << p << " " << a << " " << b << endl;
      if(a > 0) que.push(a);
      if(b > 0) que.push(b);
      //priority_queue<int> tmp(que);
      //while(tmp.size()) cout << tmp.top() << " "; cout << endl;
    }
    cout << "Case #" << i+1 << ": " << max(a, b) << " " << min(a, b) << endl;
  }

  return 0;
}
