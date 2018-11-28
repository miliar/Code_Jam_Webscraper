#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

void solve() {
  ull n,k;
  cin >> n >> k;

  priority_queue<ull> heap;
  heap.push(n);
  for(ull i = 0;i<k-1;i++) {
    ull a = heap.top();
    heap.pop();
    if(a % 2 == 0) {
      ull b = a / 2;
      if(b > 1) {
        heap.push(b);
        heap.push(b-1);
      }
      if(b == 1)
        heap.push(b);
    }
    else {
      ull b = (a-1) / 2;
      if(b > 0) {
        heap.push(b);
        heap.push(b);
      }
    }
  }

  if(heap.empty()) {
    cout << 0 << " " << 0;
    return;
  }

  ull a1, a2,a= heap.top();
  if(a % 2 == 0) {
    a1 = a / 2;
    if(a1 >= 1)
      a2 = a1-1;
    if(a1 == 0)
      a2 = 0;
  }
  else {
    a1 = a2 = (a-1) / 2;
  }

  cout << max(a1,a2) << " " <<  min(a1,a2);
}



int main(){
  int T;
  cin >> T;
  for(int t = 1;t<= T;t++) {
    cout << "Case #" << t << ": ";
    solve();
    cout << endl;
  }
}
