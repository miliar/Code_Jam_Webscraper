#include <bits/stdc++.h>
using namespace std;

using LLI = long long int;
using Pair = pair<LLI, LLI>;

struct Comp {
  bool operator()(const Pair &a, const Pair &b) {
    LLI al = a.second - a.first;
    LLI bl = b.second - b.first;
    if (al != bl) return al < bl;
    return a.first > b.first;
  }
};

int T;
LLI N;
LLI K;

int main() {
  scanf("%d", &T);
  for (int Case=1; Case<=T; Case++) {
    printf("Case #%d: ", Case);
    scanf("%lld%lld", &N, &K);
    priority_queue<Pair, vector<Pair>, Comp> q;
    q.push(Pair(0, N));
    for (LLI i=0; i<K-1; i++) {
      Pair p = q.top(); q.pop();
      LLI l = p.first;
      LLI r = p.second;
      LLI mid = (l+r-1)/2;
      if (l < mid) q.push(Pair(l, mid));
      if (mid+1 < r) q.push(Pair(mid+1, r));
    }
    Pair p = q.top(); q.pop();
    LLI l = p.first;
    LLI r = p.second;
    LLI mid = (l+r-1)/2;
    printf("%lld %lld\n", max(mid-l, r-mid-1), min(mid-l, r-mid-1));
  }
}
