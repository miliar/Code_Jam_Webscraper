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
    int c, j;
    int job[2][2];
    scanf("%d %d", &c, &j);
    for(int i=0; i<c+j; i++){
      scanf("%d %d", &job[i][0], &job[i][1]);
    }
    if(c+j == 1 || (c == 1 && j == 1)) printf("Case #%d: 2\n", t - T);
    else{
      if(job[0][0] > job[1][0]){
        int temp = job[0][0];
        job[0][0] = job[1][0];
        job[1][0] = temp;
        temp = job[0][1];
        job[0][1] = job[1][1];
        job[1][1] = temp;
      }
      if(job[1][1] - job[0][0] <= 720) printf("Case #%d: 2\n", t - T);
      else if((job[0][1] + 1440 - job[1][0]) % 1440 <= 720) printf("Case #%d: 2\n", t - T);
      else printf("Case #%d: 4\n", t - T);
    }
  }
  return 0;
}
