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
  int N, Q;
  while(T--){
    scanf("%d %d", &N, &Q);
    vector<long long int> dist = vector<long long int>(N, 0); // d(j, j+1)
    vector<long long int> end = vector<long long int>(N+1, 0); // E_j
    vector<long long int> speed = vector<long long int>(N+1, 0);
    long long int cdist[101][101];
    for(int i=0; i<=100; i++){
      for(int j=0; j<=100; j++){
        cdist[i][j] = 0;
      }
    }
    for(int i=1; i<=N; i++){
      cin >> end[i] >> speed[i];
    }
    long long int d;
    for(int i=1; i<=N; i++){
      for(int j=1; j<=N; j++){
        scanf("%lld", &d);
        if(i+1 == j){
          dist[i] = d;
          for(int k=1; k<=j-1; k++){
            cdist[k][j] = cdist[k][j-1] + d;
          }
        }
      }
    }
    int U, V;
    for(int i=1; i<=Q; i++){
      scanf("%d %d", &U, &V);
    }
    vector<double> time = vector<double>(N+1, 0.0f);
    for(int i=2; i<=N; i++){
      double min = 1000000000000.0f;
      for(int j=i-1; j>=1; j--){
        if(cdist[j][i] > end[j])
          continue;
        if(min > time[j] + ((double)cdist[j][i] / (double)speed[j])){
          min = time[j] + ((double)cdist[j][i] / (double)speed[j]);
        }
      }
      time[i] = min;
    }
    printf("Case #%d: %.9f\n", t - T, time[N]);
  }
  return 0;
}
