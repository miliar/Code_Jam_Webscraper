#include <iostream>
#include<queue>
#include<cstring>
#define ll long long
using namespace std;

//ll two_pow[63];
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T;
  ll n,k;
  scanf("%d",&T);
  for(int t= 1; t <= T;t++)
  {
    printf("Case #%d: ",t);
    scanf("%lld%lld",&n,&k);
    /*for(int i = 0; i <= 63;i++)
    {
      two_pow[i] = tmp <<i;
    }*/
    ll left,right;
    priority_queue<ll> qq;
    qq.push(n);
    int cnt = 0;
    int rua;
    if(n == k)
    {
      printf("0 0\n");
      continue;
    }
    while(cnt < k)
    {
      rua = qq.top();
      qq.pop();
      cnt++;
        if(rua & 1)
        {
          left = rua >>1;
          right = left;
          if(left > 0)
          qq.push(left);
          if(right > 0)
          qq.push(right);
        }
      else
      {
        left = rua >>1;
        right = left-1;
        if(left > 0)
        qq.push(left);
        if(right > 0)
        qq.push(right);
      }
    }
    printf("%lld %lld\n",left,right);

  }
return 0;
}
