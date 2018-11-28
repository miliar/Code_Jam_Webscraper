#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int t; cin >> t;

  for (int j = 1; j <= t; j++) {
    cout << "Case #" << j << ": ";
    int k, n; cin >> n >> k;
    priority_queue<int> pq;
    pq.push(n);
    int last = -1;
    for (int i = 1; i <= k; i++) {
      int cur = pq.top();
      last = cur;
      pq.pop();
      int half = (cur - 1) / 2;
      pq.push(half);
      pq.push(cur - half - 1);
    }
    int res1 = (last - 1) / 2;
    int res2 = last - res1 - 1;
    cout << max(res1, res2) << " " << min(res1, res2) << "\n";
  }

  return 0;
}
