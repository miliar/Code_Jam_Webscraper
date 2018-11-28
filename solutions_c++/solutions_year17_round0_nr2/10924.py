#include<bits/stdc++.h>
using namespace std;
bool ans(unsigned long long x)
{
  unsigned long long d=x%10;
  x=x/10;
  while(x)
  {
    if(!(d>=x%10))
      return false;
    d=x%10;
    x=x/10;
  }
  return true;
}
int main()
{
  ios::sync_with_stdio(false);
  long t,j;
  unsigned long long n,i;
  bool x;
   cin>>t;
   for(j=1;j<=t;j++)
   {
     cin>>n;
     for(i=n;i>=1;i--)
     {
        x=ans(i);
        if(x)
        {
          cout<<"Case #"<<j<<": "<<i<<"\n";
          break;
        }
     }
   }

  return 0;
}
