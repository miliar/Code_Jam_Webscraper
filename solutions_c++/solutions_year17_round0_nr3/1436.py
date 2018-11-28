#include <iostream>
#include <algorithm>
#include <tuple>
#include <queue>
using namespace std;
using i64 = long long;

int n;

pair<int, int> solve(const vector<bool>& v, int pos) {
  int left = 0;
  for(int i=pos-1; i>=0; --i) {
    if(!v[i]) { ++left; }
    else { break; }
  }
  int right = 0;
  for(int i=pos+1; i<n; ++i) {
    if(!v[i]) { ++right; }
    else { break; }
  }
  int maxi = left, mini = right;
  if(maxi < mini) { swap(maxi, mini); }
  return make_pair(maxi, mini);
}

int len(int l, int r) { return r - l; }

pair<int, int> f(int N, int K) {
  ::n = N + 2;
  vector<bool> v(n, false);
  v[0] = true;
  v[n-1] = true;
  priority_queue<tuple<int, int, int, int>, vector<tuple<int, int, int, int>>, greater<tuple<int, int, int, int>>> que;
  que.emplace(0, -len(1, n-1), 1, n-1);
  int cnt = 0;
  int depth, _, l, r;
  while(!que.empty()) {
    tie(depth, _, l, r) = que.top(); que.pop();
    int length = r - l;
    if(length == 0) { continue; }
    if(length & 1) {
      int pos = l + length / 2;
      v[pos] = true;
      if(++cnt == K) { return solve(v, pos); }
      que.emplace(depth+1, -len(l, pos),   l,     pos);
      que.emplace(depth+1, -len(pos+1, r), pos+1, r);
    } else {
      int pos = l + length / 2 - 1;
      v[pos] = true;
      if(++cnt == K) { return solve(v, pos); }
      que.emplace(depth+1, -len(pos+1, r), pos+1, r);
      que.emplace(depth+1, -len(l, pos),   l, pos);
    }
  }
  throw;
}

int main(void) {
  int T; scanf("%d", &T);
  int maxi, mini;
  for(int loop=0; loop<T; ++loop) {
    int N, K; scanf("%d%d", &N, &K);
    tie(maxi, mini) = f(N, K);
    printf("Case #%d: %d %d\n", loop+1, maxi, mini);
  }
  return 0;
}
