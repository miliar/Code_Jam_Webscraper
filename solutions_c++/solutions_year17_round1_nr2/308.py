#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
const int64 INF = 1LL << 58;

int64 solve()
{
  int N, P, R[50];
  multiset< int > t[50];

  cin >> N >> P;
  for(int i = 0; i < N; i++) {
    cin >> R[i];
  }
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < P; j++) {
      int s;
      cin >> s;
      t[i].emplace(s);
    }
  }

  int64 ret = 0;
  for(int i = 0; i < 56000000; i++) {
    int64 highest = INF;
    for(int j = 0; j < N; j++) {
      int64 low = (1LL * R[j] * i * 9 + 9) / 10;
      int64 high = (1LL * R[j] * i * 11) / 10;
      if(t[j].empty() || low > *--t[j].end()) return (ret);
      int64 proc = 0;
      for(auto &p : t[j]) proc += low <= p && p <= high;
      highest = min(highest, proc);
    }
    if(highest > 0) {
      for(int j = 0; j < N; j++) {
        int64 low = (1LL * R[j] * i * 9 + 9) / 10;
        int64 high = (1LL * R[j] * i * 11) / 10;
        int64 proc = 0;
        for(multiset< int >::iterator it = t[j].begin(); it != t[j].end();) {
          if(low <= *it && *it <= high) {
            it = t[j].erase(it);
            ++proc;
          } else {
            ++it;
          }
          if(proc == highest) break;
        }
      }
      ret += highest;
    }
  }
  return (ret);
}

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
}
