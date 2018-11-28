#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
  int T; cin>>T;
  for(int t=1; t<=T; t++){
    int n, k; cin>>n>>k;

    priority_queue<int>pq;
    pq.push(n);
    int l,r;
    for(int i=0;i<k;i++){
      int x=pq.top();
      pq.pop();

      l=x/2;
      r=(x-1)/2;

      pq.push(l);
      pq.push(r);
    }
    printf("Case #%d: %d %d\n", t, max(l,r), min(l,r));
  }
}
