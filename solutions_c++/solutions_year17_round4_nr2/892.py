#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int cont[1001][1001];

int main(){
  int T;

  scanf("%d",&T);

  for(int tc = 1;tc <= T;++tc){
    memset(cont,0,sizeof cont);

    int N,C,M;

    scanf("%d %d %d",&N,&C,&M);

    for(int i = 0,p,b;i < M;++i){
      scanf("%d %d",&p,&b);
      ++cont[b][p];
    }

    int rides = 0;

    for(int b = 1;b <= C;++b){
      int sum = 0;

      for(int p = 1;p <= N;++p){
        sum += cont[b][p];
      }

      rides = max(rides, sum);
    }

    for(int p = 1;p <= N;++p){
      int sum = 0;

      for(int b = 1;b <= C;++b){
        sum += cont[b][p];
      }
      //printf("%d %d\n",p,sum);
      rides = max(rides, (sum + p - 1) / p);
    }

    int prom = 0;

    for(int p = 1;p <= N;++p){
      int sum = 0;

      for(int b = 1;b <= C;++b){
        sum += cont[b][p];
      }

      if(sum > rides) prom += sum - rides;
    }

    printf("Case #%d: %d %d\n", tc, rides, prom);
  }

  return 0;
}
