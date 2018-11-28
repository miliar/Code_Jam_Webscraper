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

int main()
{ ll t,g=1;
  cin>>t;
  
  while(t--)
  { ll n,k,val;
    cin>>n>>k;
    
    set<ll>s;
    ll u,v;

    map<ll,ll> mp;
    mp[n]=1;
    s.insert(n);
    ll p;

    while(k>0)
    { p=*s.rbegin();
      val=min(k,mp[p]);
      k-=val;
      
      if(k==0)
      { u=p/2;
        v=p/2;
        if(p%2==0)
        --v;	
      }	

      if(p&1 && p>1)
      { mp[p/2]+=2*mp[p];
        s.insert(p/2);
      }
      else if(p>0)
      { mp[p/2]+=mp[p];
        s.insert(p/2);

        if(p/2>1)
        { mp[p/2-1]+=mp[p];
          s.insert(p/2-1);
        }    
      }

      mp[p]-=val;
      if(mp[p]==0)
      s.erase(p);	
    }	
       
      cout<<"Case #"<<g<<": "<<u<<" "<<v<<"\n";
      ++g;
  }
	
  return 0;
}