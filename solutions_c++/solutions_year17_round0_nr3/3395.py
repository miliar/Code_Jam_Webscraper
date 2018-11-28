#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <queue>

using namespace std;

#define FILENAME "C-small-2-attempt0.in"

pair<int, int> solve (int n, int k) {
  priority_queue<int> data;
  data.push(n + 1);
  int ans1, ans2;
  for (int i = 0; i < k; ++i) {
    int d = data.top();
    data.pop();
    int val1 = d / 2, val2 = d - d / 2;
    ans1 = val2 - 1;
    ans2 = val1 - 1;
    data.push(val1);
    data.push(val2);
  }
  return make_pair(ans1, ans2);
}

int main() {
  freopen(FILENAME, "r", stdin); freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
      int n, k;
    cin >> n >> k;
    pair<int, int> temp = solve(n, k);
    cout << "Case #" << i << ": " << temp.first << " " << temp.second << endl;
  }
  int n, k;
  cin >> n >> k;
  solve(n, k);
  return 0;
}
