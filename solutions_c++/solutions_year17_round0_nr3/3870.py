#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
  int t, k, n;
  
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> n >> k;
    priority_queue<int> pq;
    pq.push(n);
    for(int j = 0; j < k-1; j++) {
      int s = pq.top();
      if(s>1) {
        pq.pop();
        pq.push((s-1)/2);
        pq.push((s-1)-(s-1)/2);
      }
    }
    int m = pq.top();
    int mi = min((m-1)/2,(m-1)-(m-1)/2);
    int ma = m-mi-1;
    cout << "Case #" << i << ": " << ma << " " << mi << endl; 
  }
  return 0;
}