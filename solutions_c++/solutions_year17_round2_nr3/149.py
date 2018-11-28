#include <stdio.h>

int e[100000];
int s[100000];
long long d[2000][2000];
long double time[2000][2000];
int main() {
  int t;
  scanf("%d",&t);
  for(int g = 0 ; g< t;g++) {
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i = 0 ; i < n ; i++) { 
      scanf("%d%d", &e[i],&s[i]);
    }
    for(int i = 0 ; i< n ; i++) {
      for(int j = 0 ;j < n ; j++) {
        scanf("%lld",&d[i][j]);
      }
    }
    for(int k = 0 ; k < n ; k++) {
      for(int i = 0 ; i < n ; i++) {
        for(int j = 0 ; j< n ; j++) {
          if (d[i][k] != -1 && d[k][j] != -1 && (d[i][k] + d[k][j] < d[i][j] || d[i][j] == -1)) {
            d[i][j] = d[i][k] + d[k][j];
          }
        }
      }
    }
    for(int i = 0 ; i < n ; i++) {
      for(int j = 0 ; j < n ; j++) {
        if (d[i][j] != -1 && d[i][j] <= e[i]) {
          time[i][j] = ((double)d[i][j]) / s[i];
        } else {
          time[i][j] = -1;
        }
      }
    }
    for(int k = 0 ; k < n ; k++) {
      for(int i = 0 ; i < n ; i++) {
        for(int j = 0 ; j< n ; j++) {
          if (time[i][k] != -1 && time[k][j] != -1 && (time[i][k] + time[k][j] < time[i][j] || time[i][j] == -1)) {
            time[i][j] = time[i][k] + time[k][j];
          }
        }
      }
    }
    // if (g == 6) {
    //   for(int i = 0 ; i < n ;i++) {
    //     for(int j = 0 ;j < n ;j++) printf("%lld ", d[i][j]);
    //     printf("\n");
    //   }
    //   printf("\n");
    //   for(int i = 0 ; i < n ;i++) {
    //     for(int j = 0 ;j < n ;j++) printf("%lf ", time[i][j]);
    //     printf("\n");
    //   }
    //   printf("\n");
    // }

    printf("Case #%d:", g+1);
    for(int k = 0 ; k < m ; k++) {
      int x,y;
      scanf("%d%d",&x,&y);
      x--;y--;
      printf(" %.9Lf", time[x][y]);
    }
    printf("\n");
  }
}
