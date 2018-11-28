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
  int N, K;
  int t, T;
  scanf("%d", &T);
  t = T;
  while(T--){
    scanf("%d %d", &N, &K);
    vector<long long int> prob = vector<long long int>(N+1);
    int up, dp;
    scanf("%d.%d", &up, &dp);
    int U = up * 10000 + dp;
    for(int i=0; i<N; i++){
      scanf("%d.%d", &up, &dp);
      prob[i] = up * 10000 + dp;
    }
    prob[N] = 10000;
    vector<double> p = vector<double>(N);
    for(int i=0; i<N; i++){
      p[i] = (double)prob[i];
    }
    sort(prob.begin(), prob.end());
    int aim = 1;
    while(U > 0 && aim <= N){
      if(prob[aim-1] == prob[aim]){
        aim++;
        continue;
      }
      else{
        int dif = prob[aim] - prob[aim-1];
        if(U >= dif * aim){
          for(int i=0; i<aim; i++){
            prob[i] += dif;
          }
          U -= dif * aim;
        }
        else{
          int ad = U / aim;
          int re = U % aim;
          for(int i=0; i < aim; i++){
            prob[i] += ad;
          }
          for(int i = aim - re; i<aim; i++){
            prob[i]++;
          }
          U = 0;
        }
      }
    }
    double fin = 1.0f;
    for(int i=0; i<N; i++){
      fin *= (double)prob[i] / double(10000);
    }
    printf("Case #%d: %.6f\n", t - T, fin);
  }
  return 0;
}
