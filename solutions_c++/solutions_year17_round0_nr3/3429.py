#include<bits/stdc++.h>
using namespace std;

int main (void) {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int n, k;
    cin >> n >> k;
    priority_queue<int> pq;
    pq.push(n);
    for (int i = 0; i < k-1; i++) {
      int next = pq.top() - 1;
      pq.pop();
      pq.push(next/2);
      pq.push(next-next/2);
    }
    int next = pq.top() - 1;
    pq.pop();
    printf("Case #%d: %d %d\n",tt,next-next/2,next/2);
  }
}
