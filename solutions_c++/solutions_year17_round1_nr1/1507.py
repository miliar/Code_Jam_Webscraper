#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define MOD 1000000007
#define M(x) (x%MOD + MOD)%MOD
#define _pb push_back
#define _mp make_pair
#define ff first
#define ss second
#define sc(x) scanf("%lld",&x)
 
ll mul(ll x,ll y)
{ ll ans=1;
 
  while(y>0)
 { if(y&1)
   ans=(ans*x)%MOD;
   x=(x*x)%MOD;
   y/=2;
 }
 
 return ans;
};
 
//.............................................................
char a[50][50];

int main()
{ ll t,g=1;
  sc(t);

   while(t--)
  { ll r,c,i,j,k;
    sc(r); sc(c);
    
    for(i=1;i<=r;i++)
    for(j=1;j<=c;j++) 
    cin>>a[i][j];
    
    for(i=1;i<=r;i++)
    for(j=1;j<=c;j++)
    if(a[i][j]!='?')
    { 
      for(k=j+1;k<=c;k++)
      if(a[i][k]=='?')
      a[i][k]=a[i][j];
      else
      break;	
      
      for(k=j-1;k>=1;k--)
      if(a[i][k]=='?')
      a[i][k]=a[i][j];
      else
      break;
    }

    for(i=1;i<=r;i++)
    for(j=1;j<=c;j++)
    if(a[i][j]!='?')
    { for(k=i-1;k>=1;k--)
      if(a[k][j]=='?')
      a[k][j]=a[i][j];
      else
      break;

      for(k=i+1;k<=r;k++)
      if(a[k][j]=='?')
      a[k][j]=a[i][j];
      else
      break;     
    }	
     
     cout<<"Case #"<<g<<":\n";

     for(i=1;i<=r;i++)
     { for(j=1;j<=c;j++)
       cout<<a[i][j];
       cout<<"\n";
     }	
     ++g;

  }	
  return 0;
}