#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 100005

map<ll, map<ll, ll> > cnt;
void dfs(ll x) {
  if (cnt.find(x) != cnt.end()) return;
  if (x == 0) return;
  ll lx = x / 2, rx = (x - 1) / 2;
  dfs(lx);
  dfs(rx);
  map<ll, map<ll, ll> >::iterator lr = cnt.find(lx), rr = cnt.find(rx);
  cnt[x][x] = 1;
  if (lr != cnt.end()) {
    map<ll,ll> &m = lr->second;
    for (map<ll,ll>::iterator r = m.begin(); r != m.end(); r++) {
      cnt[x][r->first] += r->second;
    }
  }
  if (rr != cnt.end()) {
    map<ll,ll> &m = rr->second;
    for (map<ll,ll>::iterator r = m.begin(); r != m.end(); r++) {
      cnt[x][r->first] += r->second;
    }
  }
}
int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    ll N, K;
    cin >> N >> K;
    cnt.clear();
    dfs(N);
    ll sum = 0;
    for (map<ll,ll>::reverse_iterator r = cnt[N].rbegin(); r != cnt[N].rend(); r++) {
      if (sum + 1 <= K && sum + r->second >= K) {
        ll x = r->first;
        cout << x / 2 << " " << (x - 1) / 2 << endl;
        break;
      } else sum += r->second;
    }
  }
  return 0;
}
