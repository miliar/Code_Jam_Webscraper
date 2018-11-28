#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

#define int long long
typedef pair<long long, long long> P;
#define rep(i, n) for (int i=0; i<(n); i++)
#define all(c) (c).begin(), (c).end()
#define uniq(c) c.erase(unique(all(c)), (c).end())
#define _1 first
#define _2 second
#define pb push_back
#define INF 1145141919
#define MOD 1000000007

int T;
map<long long, long long> C;

P solve(long long n, long long k) {
  priority_queue<long long> q;
  q.push(n);
  C.clear();
  C[n] = 1;

  long long a = -1, b = -1;
  while (k > 0 && !q.empty()) {
    long long r = q.top();
    q.pop();
    long long x = C[r];
    if (x == 0) continue;

    long long mid = (r-1)/2;
    a = mid;
    b = r-1-mid;
    q.push(a);
    C[a] += x;
    q.push(b);
    C[b] += x;
    C[r] = 0;
    k -= x;
  }
  if (a < b) swap(a, b);
  return P(a, b);
}

signed main() {
  ios::sync_with_stdio(false); cin.tie(0);
  cin >> T;
  rep(i, T) {
    long long n, k;
    cin >> n >> k;
    P a = solve(n, k);
    cout << "Case #"<<i+1<<": "<<a._1 << " " << a._2 << "\n";
  }
  return 0;
}
