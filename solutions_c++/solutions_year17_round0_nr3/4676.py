#include <stdio.h>
#include <queue>
using namespace std;

struct Seg {
  int x,y,len;
  bool operator < (const Seg i) const{
    return ((len < i.len) || (len == i.len && x > i.x));
  }
};
priority_queue<Seg> list;

int main() {
  int T;
  scanf ("%d",&T);
  for (int test = 1;test <= T; test ++) {
    int N, K;
    scanf ("%d%d",&N,&K);
    list.push({1, N, N});
    int L, R;
    for (int i=1;i<=K;i++) {
      Seg s = list.top(); list.pop();
      int m = (s.x + s.y) >> 1;
      list.push({s.x,m-1,m-1-s.x+1});
      list.push({m+1,s.y,s.y-m-1+1});
      if (i == K) {
        L = s.y-m-1+1;
        R = m-1-s.x+1; 
      }
    }
    printf ("Case #%d: %d %d\n",test,L,R);
    while (!list.empty()) list.pop();
  }
  return 0;
}

