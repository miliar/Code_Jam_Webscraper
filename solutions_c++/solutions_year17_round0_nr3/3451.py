#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cout << "Case #" << (t+1) << ": ";
    long long N, K;
    cin >> N >> K;
    priority_queue<long long> *pq = new priority_queue<long long>();
    pq->push(N);
    for (long long k = 0; k < K; ++k) {
      long double e = (pq->top() - 1) / 2.0;
      pq->pop();
      if (k == K - 1) {
        cout << (long long)(e + 0.5) << " " << (long long)e << endl;
      }
      pq->push(e);
      pq->push(e + 0.5);
    }
    delete pq;
  }
  return 0;
}
