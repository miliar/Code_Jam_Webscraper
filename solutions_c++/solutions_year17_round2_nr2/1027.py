#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<set>
#include<queue>
#include<cstdlib>
#include<cmath>
#include<functional>

using namespace std;

int main(){
  int t, T;
  scanf("%d", &T);
  t = T;
  while(T--){
    int N, col[6];
    scanf("%d %d %d %d %d %d %d", &N, &col[0], &col[1], &col[2], &col[3], &col[4], &col[5]);
    vector<int> circ = vector<int>(N, -1);
    // 0: R, 1: Y, 2: B
    vector<int> r = vector<int>(N, -1);
    vector<int> y = vector<int>(N, -1);
    vector<int> b = vector<int>(N, -1);
    if(N < 2*col[0] || N < 2*col[2] || N < 2*col[4]){
      printf("Case #%d: IMPOSSIBLE\n", t - T);
      continue;
    }
    else{
      int ind = -1;
      int sec = -1;
      if(col[0]>=col[2] && col[0]>=col[4]) {
        ind = 0;
        if(col[2] >= col[4]) sec = 2;
        else sec = 4;
      }
      else if(col[2]>=col[0] && col[2]>=col[4]) {
        ind = 2;
        if(col[0] >= col[4]) sec = 0;
        else sec = 4;
      }
      else {
        ind = 4;
        if(col[0] >= col[2]) sec = 0;
        else sec = 2;
      }
      int last = N - 2 * col[ind];
      int i=0;
      for(i=0; i<last; i++){
        circ[3*i] = ind;
      }
      for(i=last; i<col[ind]; i++){
        circ[3*last + 2*(i-last)] = ind;
      }
      for(i=0; i<(last < col[sec] ? last : col[sec]); i++){
        circ[3*i + 1] = sec;
      }
      for(i=last; i<col[sec]; i++){
        circ[3*last + 1 + 2*(i-last)] = sec;
      }
      for(i=0; i<N; i++){
        if(circ[i] == -1) circ[i] = 6 - ind - sec;
      }
      printf("Case #%d: ", t - T);
      for(i=0; i<N; i++){
        if(circ[i] == 0) printf("R");
        else if(circ[i] == 2) printf("Y");
        else printf("B");
      }
      printf("\n");
    }
  }
  return 0;
}
