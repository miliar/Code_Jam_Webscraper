#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  for(int x=0;x<T;x++){
    printf("Case #%d: ",x+1);
    int n,q;
    scanf("%d %d",&n,&q);
    int e[200],s[200];
    for(int i=0;i<n;i++){
      scanf("%d %d",&e[i],&s[i]);
    }
    long d[200][200],dist[200];
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        scanf("%d",&d[i][j]);
      }
    }
    int u,v;
    scanf("%d %d",&u,&v);
    double time[200][200];
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        time[i][j] = -1.0;
      }
    }
    dist[0] = 0;
    for(int i=1;i<n;i++){
      dist[i] = dist[i-1] + d[i-1][i];
    }
    for(int i=0;i<n;i++){
      double min_time = 0;
      if(i != 0){
        min_time = 99999999999999999.0;
        for(int k = 0; k < i; k ++){
          if(time[k][i] > 0)
            min_time = min(min_time, time[k][i]);
        }
      }
      for(int j=i+1;j<n;j++){
        if(dist[j] - dist[i] <= e[i]){
          time[i][j] = min_time + (dist[j]-dist[i]) / (double)s[i];
        }
      }
    }
    double ans = 9999999999999999999.0;
    for(int i=0;i<n;i++){
      if(time[i][n-1] > 0)
        ans = min(ans,time[i][n-1]);
    }
    // for(int i=0;i<n;i++){
    //   for(int j=0;j<n;j++){
    //     printf("%lf ",time[i][j]);
    //   }
    //   printf("\n");
    // }
    printf("%lf\n",ans);
  }
}
