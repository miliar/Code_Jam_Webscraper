#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <utility>

using namespace std;

map<long long, long long, greater<long long> > q;

int main() {
  int num;
  cin >> num;
  for (int i = 1; i <= num; i++) {
    long long N, K;
    pair<long long, long long> res;
    cin >> N >> K;
    q.clear();
    q.insert(make_pair(N, 1));
    while (K > 0) {
      auto p = *q.begin();
      auto n = p.first - 1;
      auto times = p.second;
      K -= times;
      auto l = n / 2, r = n - l;
      q.erase(q.begin());
      res.first = max(l, r);
      res.second = min(l, r);
      if (r > 0) q[r] += times;
      if (l > 0) q[l] += times;
    }
    cout << "Case #" << i << ": " << res.first << " " << res.second << endl;
  }
  return 0;
}
