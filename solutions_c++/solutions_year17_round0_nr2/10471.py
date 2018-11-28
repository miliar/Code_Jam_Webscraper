#include<bits/stdc++.h>
using namespace std;
char s[10000000];
int main()
{
    long long n,t,i,j,k,l,m,a1,ans,f;
    cin>>t;m=1;
    while(t--)
     {
          cin>>n;
          while(n)
          {f=0;
              j=n%10;ans=n;
              for(i=n/10;i>0;i=i/10)
              {
                  k=i%10;
                  if(k<=j)
                  {
                    f=0;j=k;
                  }
                  else
                  {
                      f=1;
                      break;
                  }
              }
              if(f==0)
              {
                  cout<<"Case #"<<m<<": "<<ans<<"\n";break;
              }
              n--;

          }
          m++;
     }

    return 0;
}
