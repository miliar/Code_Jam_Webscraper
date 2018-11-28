#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cn = 1;cn <= T;cn++) {
    int n,k;
    cin >> n >> k;
    priority_queue<pair<int,int>> pq;
    pq.push({n,-1});
    int r1,r2;
    for (int i = 0;i < k;i++) {
      auto pos = pq.top();
      pq.pop();
      pair<int,int> s1 = {(pos.first-1) >> 1,pos.second};
      pair<int,int> s2 = {pos.first >> 1, - (-pos.second + ( (pos.first-1)>> 1)+1) };
      if (s1.first > 0) pq.push(s1);
      if (s2.first > 0) pq.push(s2);
//      printf("--- step %d ----\ngot %d %d\n",i+1,pos.first, -pos.second);
//      if (s1.first > 0) printf("put %d %d\n",s1.first, -s1.second);
//      if (s2.first > 0) printf("put %d %d\n",s2.first, -s2.second);
      if (i == k-1) {
        r1 = s2.first;
        r2 = s1.first;
      }
    }
    printf("Case #%d: %d %d\n",cn,r1,r2);
  }
}

