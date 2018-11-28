#include<bits/stdc++.h>
using namespace std ;
typedef long long ll ;
bool chk(ll n)
{ int prev=INT_MAX ;
  while(n>0)
  { int d=n%10 ;
    if(prev<d)
     return 0 ;
    prev=d ;
    n/=10 ;
  }
  return 1 ;
}
int main()
{ cin.sync_with_stdio(false) ;
  freopen("input.in","rt",stdin) ;
  freopen("output.txt","wt",stdout) ;
  int t,i=0 ;
  cin>>t ;
  while(i<t)
  { ll n ;
    cin>>n ;
    while(!chk(n))
    { n=n-n%10-1 ;
    }
    cout<<"Case #"<<i+1<<": "<<n<<"\n" ;
    i++ ;
  }
  return 0 ;
}
