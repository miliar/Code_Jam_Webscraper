#include <bits/stdc++.h>

using namespace std;

typedef long long int64;

pair< int64, int64 > getPair(int64 cur)
{
  --cur;
  return {(cur + 1) / 2, cur / 2};
}


void solve()
{
  int64 N, K;
  cin >> N >> K;

  map< pair< int64, int64 >, int64 > que;
  que[getPair(N)]++;
  --K;

  if(K == 0) {
    cout << getPair(N).first << " " << getPair(N).second << endl;
    return;
  }

  for(;;) {
    auto object = *--que.end();

    int64 get = min(K, object.second);
    K -= get;

    if(K == 0 && get <= object.second) {
      auto q = getPair(object.first.first);
      cout << q.first << " " << q.second << endl;
      return;
    }
    if(get > 0) que[getPair(object.first.first)] += get;

    get = min(K, object.second);
    K -= get;
    if(K == 0 && get <= object.second) {
      auto q = getPair(object.first.second);
      cout << q.first << " " << q.second << endl;
      return;
    }
    if(get > 0) que[getPair(object.first.second)] += get;
    que.erase(--que.end());
  }
}

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
}
