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
    int n,m,t,i,j,q,type,l,r,p,len,siz,ans,res,sum,a,b,c,k,x;
    
    ll ans1,ans2;
    
    vector<ll>::iterator it;
 
    
    cin>>t;
    
    j=1;
    
    while(t--)
    {
    	cout<<"Case #"<<j<<": \n";
    	
    	cin>>r>>c;
    	
    	char ar[r+1][c+1];
    	
    	for(i=0;i<r;i++)
    	{
    		for(k=0;k<c;k++)
    		{
    			cin>>ar[i][k];
			}
		}
		
		for(k=0;k<c;k++)
    	{
    		for(i=0;i<r;i++)
    		{
    			   if(ar[i][k]!='?')
    			{
    			    x=i+1;
    			    while(ar[x][k]=='?' && x<r)
    			    {
    			        ar[x][k]=ar[i][k];
    			        x++;
    			    }
				}
			}
		}
		
		for(k=0;k<c;k++)
    	{
    		for(i=r-1;i>=0;i--)
    		{
    			   if(ar[i][k]!='?')
    			{
    			    x=i-1;
    			    while(ar[x][k]=='?' && x>=0)
    			    {
    			        ar[x][k]=ar[i][k];
    			        x--;
    			    }
				}
			}
		}
		
		for(i=0;i<r;i++)
    	{
    		for(k=0;k<c;k++)
    		{
    			   if(ar[i][k]!='?')
    			{
    			    x=k+1;
    			    while(ar[i][x]=='?' && x<c)
    			    {
    			        ar[i][x]=ar[i][k];
    			        x++;
    			    }
				}
			}
		}
		
			for(i=0;i<r;i++)
    	{
    		for(k=c-1;k>=0;k--)
    		{
    			   if(ar[i][k]!='?')
    			{
    			    x=k-1;
    			    while(ar[i][x]=='?' && x>=0)
    			    {
    			        ar[i][x]=ar[i][k];
    			        x--;
    			    }
				}
			}
		}
		
		for(i=0;i<r;i++)
    	{
    		for(k=0;k<c;k++)
    		{
    			cout<<ar[i][k];
			}
			
			cout<<"\n";
		}
		
		
    	
    	j++;
	}
   
  
    
 
    return 0;
}