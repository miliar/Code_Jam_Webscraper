#include <bits/stdc++.h>

using namespace std;

int main(){
  int casos, n, k, maxi, mini;
  cin >> casos;
  for(int caso = 1 ; caso <= casos; caso++) {
    cin >> n >> k;
    priority_queue<int> pq;
    pq.push(n);
    for (int i = 0; i < k ; i++){
      int largest = pq.top() - 1; pq.pop();
      int a = largest / 2;
      int b = largest - a;
      pq.push(a);
      pq.push(b);
      maxi = max(a, b);
      mini = min(a, b);
    }
    cout << "Case #" << caso << ": " << maxi << " " << mini << endl;
  }
  return 0;
}