#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

int T;
int N, K;

int main(){

  scanf("%d ", &T);
  for (int cas=1; cas<=T; cas++){
    scanf("%d %d ", &N, &K);
    priority_queue<int> q;
    q.push(N);

    int mx = N, mn = N;
    for (int i=1; i<=K; i++){
      int r = q.top();
      q.pop();
      mx = r / 2;
      mn = (r - 1) /2;
      //printf("%d %d\n", mx, mn);
      q.push(mx);
      q.push(mn);
    }

    printf("Case #%d: %d %d\n", cas, mx, mn);
  }

  return 0;
}
