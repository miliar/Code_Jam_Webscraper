#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << #x << " = " << x << endl;


#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 10000

void solve(){
  int d,n;
  int k,s;
  pair<int,int> horse[SIZE];
  
  scanf("%d%d",&d,&n);

  double hour = 0;
  
  for(int i=0;i<n;i++){
    scanf("%d%d",&k,&s);

    hour = max(hour, (double)(d-k)/s);
  }

  printf("%.10lf\n",d/hour);
  
}

int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){

    printf("Case #%d: ",i);

    solve();
  }
  
  return 0;
}
