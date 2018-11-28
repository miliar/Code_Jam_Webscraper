#include<bits/stdc++.h>
using namespace std;

#define LL long long
#define sc(x) scanf("%lld", &x)
#define pf(x) printf("%lld\n", x)
#define dbug(x) printf(" ### %lld\n", x)
#define mem(x,y) memset( x,y,sizeof x)
#define pb push_back
#define PI (2.0*acos(0.0))


LL strtonum(string s){long long int sm;stringstream ss(s);ss>>sm;return sm;}

LL digit[30], n, make[30], dp[20][4];

LL fun(LL i, LL dgt, LL choto, LL sum)
{
    sum=sum*10+dgt;

    if(i==n+1) return dp[i][choto]=sum;
    if(dp[i][choto]!=-1) return dp[i][choto];
    dp[i][choto]=0;

    LL hi = digit[i], xx=0;
    if(choto) hi=9;

    for(LL j=hi; j>=0; j--)
    {
        if(j>=dgt || choto!=0) xx=max(xx,fun(i+1,j,(choto|j<hi),sum));
    }
   return dp[i][choto]=xx;
}

string num;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    LL t, tc=0;
    sc(t);

  while(t--)
  {
      cin>>num;
      for(LL i=0; i<num.size(); i++) digit[i+1] = (num[i]-'0'); n = num.size();
      mem(dp,-1); LL ans = fun(1,0,0,0);
      printf("Case #%lld: %lld\n", ++tc, ans);
  }

return 0;
}
