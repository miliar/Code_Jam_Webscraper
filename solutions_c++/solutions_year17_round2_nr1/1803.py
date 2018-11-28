#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define debug 0
#define ss second
#define ff first

using namespace std;


vector<ll> vec,temp,magprime;

bool prime[10000009];

vector<ll> primes;


ll bit1[10000005];

ll bit2[10000005];

bool magical[10000002];

ll arr[10000005];
    
ll brr[10000005];

 

void update1(ll x, ll val,ll n) {
	while (x <= n) {
		bit1[x] += val;
		x += x & -x;
	}
}
 
ll query1(ll x) {
	ll sum = 0;
    while (x) {
		sum += bit1[x];
		x -= x & -x;
    }
    return sum;
}

void update2(ll x, ll val,ll n) {
	while (x <= n) {
		bit2[x] += val;
		x += x & -x;
	}
}
 
ll query2(ll x) {
	ll sum = 0;
    while (x) {
		sum += bit2[x];
		x -= x & -x;
    }
    return sum;
}

void sieve()
{
    memset(prime,true,sizeof(prime));
    prime[0]=prime[1]=false;
    
    for(ll i=2;i*i<=10000000;i++)
    {
        if(prime[i])
        {
            for(ll j=i*2;j<=10000000;j+=i)
            {
                prime[j]=false;
            }
        }
    }
    
    for(ll i=2;i<=10000000;i++)
    {
    	if(prime[i])
    	primes.push_back(i);
	}
}
 

 
 
int main()
{
    int n,m,t,i,j,q,type,l,r,p,len,siz,res,sum,a,b,c;
    
    ll ans1,ans2;
    
    vector<ll>::iterator it;
    
    double d,s,maxm,tim,x,ans,rem;
 
    
    cin>>t;
    
    j=1;
    
    while(t--)
    {
    	cout<<"Case #"<<j<<": ";
    	
    	maxm=0;
    	
    	cin>>d>>n;
    	
    	for(i=0;i<n;i++)
    	{
    		cin>>x>>s;
    		
    		rem=d-x;
    		tim=rem/s;
    		
    		maxm=max(maxm,tim);
		}
		
		ans=d/maxm;
		
	  printf("%0.9lf\n",ans);
	  j++;
    	
    	
	}
   
  
    
 
    return 0;
}