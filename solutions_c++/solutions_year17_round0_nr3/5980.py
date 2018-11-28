#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;


pair<long long, long long> solve(long long ns, long long np) {
  priority_queue<long long> q;
  q.push(ns);

  for (int i = 0; i < np - 1; i++) {
    long long nseq = q.top();
    q.pop();
    if (nseq % 2 == 0) {
      q.push(nseq / 2);
      q.push((nseq / 2) - 1);
    } else {
      q.push(nseq / 2);
      q.push(nseq / 2);
    }
  }
  long long seq = q.top();

  pair<long long, long long> ans;
  if (seq % 2 == 0) {
    ans.first = seq / 2;
    ans.second = seq / 2 - 1;
  } else {
    ans.first = seq / 2;
    ans.second = seq / 2;
  }
  return ans;
}

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    long long ns, np;
    cin >> ns >> np;
    auto ans = solve(ns, np);
    printf("Case #%d: %lld %lld\n", i+1, ans.first, ans.second);
  }
}
