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
  ll n;
  int num[20];

  scanf("%lld",&n);

  if(n == 1000000000000000000){
    puts("999999999999999999");
    return;
  }
  
  ll ans = 0;
  
  for(int i=0;i<18;i++){
    num[i] = n%10;
    n/=10;
  }

  for(int k=0;k<18;k++){
    ll ans2 = 0, t = 1;
    int num2[20] = {};
    
    for(int i=0;i<18;i++){
      if(i < k){
        num2[i] = 9;
      }else if(i == k){
        if(num[i] == 0){
          ans2 = 0;
          break;
        }
        if(i > 0) num2[i] = num[i]-1;
        else num2[i] = num[i];
      }else if(i > 0){
        num2[i] = min(num2[i-1],num[i]);
      }
      ans2 += num2[i] * t;
      t *= 10;
    }

    ans = max(ans, ans2);
  }

  printf("%lld\n",ans);
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
