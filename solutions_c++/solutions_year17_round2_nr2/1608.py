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
    int n,m,t,i,j,q,type,l,r,p,len,siz,ans,res,sum,a,b,c;
    
    ll ans1,ans2;
    
    vector<ll>::iterator it;
    priority_queue<pair<int,char> > pq;
	
	map<char,int> freq;
	pair<int,char> k;
 
    
    cin>>t;
    
    j=1;
    
    while(t--)
    {
    	cout<<"Case #"<<j<<": ";
    	
    	freq.clear();
    	
    	cin>>n;
    	
    	for(i=0;i<6;i++)
    	{
    		cin>>p;
    		
    		if(p==0)
    		continue;
    		
    		if(i==0)
    		{
    			freq['R']=p;
			}
			else if(i==1)
			{
				freq['O']=p;
			}
			else if(i==2)
			{
				freq['Y']=p;
			}
			else if(i==3)
			{
				freq['G']=p;
			}
			else if(i==4)
			{
				freq['B']=p;
			}
			else if(i==5)
			{
				freq['V']=p;
				
			}
		}
    	
    	for(char i='A';i<='Z';i++)
	    {
	        if(freq[i])
	        {
	            pq.push(mp(freq[i],i));
	        }
	    }
	    
	    pair<int,char> p={-1,'A'};
	    
	    string ptr="";
	    
	    while(!pq.empty())
	    {
	        k=pq.top();
	        
	        ptr+=k.second;
	        
	        pq.pop();
	        
	        if(p.first>0)
	        pq.push(p);
	        
	        k.first--;
	        p=k;
	    }
	    
	    //cout<<ptr<<"\n";
	    
	     if(ptr.length()==n)
	     {
	         len=ptr.length();
	    
	       if(ptr[0]==ptr[len-1])
	       {
	           
	           if(len>=3 && ptr[len-1]!=ptr[len-3])
	           {
	               swap(ptr[len-1],ptr[len-2]);
	               cout<<ptr<<"\n";
	           }
	           else if(len>=4 && ptr[len-1]!=ptr[len-4] && ptr[len-1]!=ptr[len-3])
	           {
	               swap(ptr[len-1],ptr[len-3]);
	               cout<<ptr<<"\n";
	           }
	           else if(len>=5 && ptr[len-1]!=ptr[len-5] && ptr[len-1]!=ptr[len-4])
	           {
	               swap(ptr[len-1],ptr[len-4]);
	               cout<<ptr<<"\n";
	           }
	           else
	           cout<<"IMPOSSIBLE\n";
	        }
	       else
	       cout<<ptr<<"\n";
	     }
	    else
	    cout<<"IMPOSSIBLE\n";
	    
	    j++;
    	
	}
   
  
    
    return 0;
}