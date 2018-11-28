#include <iostream>
#include <queue>
#include <cmath>
#include <algorithm>

typedef unsigned long ul;
using namespace std;


int main() {
  ul t, n, k;
  cin >> t;

  for (ul i = 0; i < t; ++i) {
    cin >> n >> k;

    priority_queue<ul> islands;
    islands.push(n);

    for (ul j = 0; j < k; ++j) {
      ul nLargest = islands.top();
      islands.pop();

      ul Ls = ceil(nLargest/2.0) - 1,
         Rs = nLargest - ceil(nLargest/2.0);

      islands.push(Ls);
      islands.push(Rs);
      if (j == k - 1)
        std::cout << "Case #" << i + 1 << ": " << max(Ls, Rs) << " " << min(Ls, Rs) << "\n";
    }
  }
}
