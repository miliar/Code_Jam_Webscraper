#include <stdio.h>
#include <math.h>
#include <queue>
#include <vector>
using namespace std;

#define mp make_pair

int cst[55];
priority_queue<int> q[55]; // -(right bound)
vector< pair<int, int> > v[1500005];

int main(){
  int T;
  scanf("%d", &T);
  for(int tc=1; tc<=T; tc++){
    int N, P;
    scanf("%d%d", &N, &P);
    for(int i=0; i<N; i++) scanf("%d", &cst[i]);
    for(int i=0; i<55; i++){
      while(!q[i].empty()) q[i].pop();
    }
    for(int i=0; i<1500005; i++) v[i].clear();
    int res = 0;
    for(int i=0; i<N; i++){
      for(int j=0; j<P; j++){
        int x;
        scanf("%d", &x);
        int r = floor((long double)x/cst[i]/0.9);
        int l = ceil((long double)x/cst[i]/1.1);
        if(l > r) continue;
        v[l].push_back(mp(i, r));
      }
    }
    for(int i=1; i<1500005; i++){
      for(int j=0; j<v[i].size(); j++) q[v[i][j].first].push(-v[i][j].second);
      int valid = 1;
      for(int j=0; j<N; j++){
        while((!q[j].empty()) && -q[j].top() < i) q[j].pop();
        if(q[j].empty()) valid = 0;
      }
      if(valid == 0) continue;
      while(valid){
        for(int j=0; j<N; j++) q[j].pop();
        for(int j=0; j<N; j++){
          while((!q[j].empty()) && -q[j].top() < i) q[j].pop();
          if(q[j].empty()) valid = 0;
        }
        res++;
      }
    }
    printf("Case #%d: %d\n", tc, res);
  }
  return 0;
}
