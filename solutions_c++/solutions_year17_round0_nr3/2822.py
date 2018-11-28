#include "bits/stdc++.h"
using namespace std;

using lld = long long;
lld level1(lld n)
{

lld c=0;
while(n>1)
  {

   c++;
   n/=2;

  }

  return c;
}
lld Pow(lld a,lld b)
{
   lld res=1;
   while(b>0)
   {

    if(b%2==1)
        res*=a;
        a*=a;
        b/=2;


   }

return res;

}
int main(){
        freopen("in1.txt","r",stdin);
        freopen("FINAL.txt","w",stdout);
   int t;
   cin>>t;
     for(int i=1;i<=t;i++)
    {
    lld n,k;
     cin>>n>>k;
      lld level=level1(k);
     lld ans=(n-k+Pow(2,level));
       ans=ans/Pow(2,level);
    lld mx,mn;
    if(ans%2==0)
    {
       mx=ans/2;
       mn=ans/2-1;


    }
    else
    {
     mx=ans/2;
       mn=ans/2;
       }
       printf("Case #%d: %lld %lld\n",i,mx,mn);

    }
}
