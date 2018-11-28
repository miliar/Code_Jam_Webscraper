#include <stdio.h>
#include <cstring>
#include <string>

typedef long long LL;
const int N=30;
char digit[N];
LL dp[2][N][10];

LL dfs(int s,int k, int x){
  if(k==19){
    return 1;
  }
  LL &ret=dp[s][k][x];
  if(ret!=-1) return ret;
  k++;
  ret=0;
  for(int i = x;i<= (s==0?9:digit[k]-'0');++i){
    ret += dfs(s&&(i==digit[k]-'0'),k,i);
  }
  //printf("%d %d %d %lld\n",s,k,x,ret);
  return ret;
}

LL get(LL v){
  memset(dp,-1,sizeof(dp));
  snprintf(digit,30,"%020lld",v);
  LL res=dfs(1,0,0);
  return res;
}

LL solve(LL n)
{
  LL l(1),r(n);
  //LL l(1),r(1);
  LL sum=get(n);
  while(l<r){
    LL mid=l+(r-l)/2;
    LL cnt=get(mid);
    if(cnt >= sum){
      r=mid;
    }else{
      l=mid+1;
    }
  }
  return r;
}

int main()
{
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  //freopen("b.out","w",stdout);

  int test,cas(1);
  LL n;
  scanf("%d",&test);
  while(test--){
    scanf("%lld",&n);
    //printf("%lld\n",get(128));
    printf("Case #%d: %lld\n",cas++,solve(n));
  }


  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
