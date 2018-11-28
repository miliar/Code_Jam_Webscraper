#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;


int main() {
  int T;
  typedef unsigned long long int ulli;
  ulli N, K, temp, l, r;

  cin >> T;

  for(int t = 0; t < T; ++t) {
    priority_queue<ulli> q;
    cout << "Case #" << (t+1) << ": ";
    cin >> N >> K;

    // Just save time
    if (N == K) {
      cout << "0 0" << endl;
      continue;
    }

    q.push(N);
    for(ulli k = 0; k < K; k++) {
      temp = q.top();
      q.pop();

      l = ceil(temp/2.0)-1;
      r = temp - l - 1;
      q.push(l);
      q.push(r);
    }
    cout << max(l,r) << ' ' << min(l,r) << endl;
  }

  return 0;
}
