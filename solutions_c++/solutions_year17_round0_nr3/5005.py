#include <bits/stdc++.h>
using namespace std;
#define ll long long




int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {
      ll N, K;
      cin >> N >> K;

      priority_queue<ll> pq;

      pq.push(N);
      for(ll i = 0; i < K - 1; i++) {
        ll pq_top = pq.top();
        pq.pop();

        pq_top -= 1;
        pq.push(pq_top / 2);
        pq.push(pq_top - pq_top / 2);
      }

      ll pq_top = pq.top() - 1;
      cout << "Case #" << t + 1 << ": " << pq_top - pq_top / 2<< ' ' << pq_top / 2 << endl;

  }
}
