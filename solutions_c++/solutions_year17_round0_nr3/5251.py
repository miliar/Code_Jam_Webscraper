/*  chuckie   */
#include <bits/stdc++.h>
#define CHUCKIE
 
#define cint(d) scanf("%d", &d)
#define cint2(a, b) scanf("%d %d", &a, &b)
#define cint3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define cint4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)
 
#define clong(d) scanf("%lld", &d)
#define clong2(a, b) scanf("%lld %lld", &a, &b)
#define clong3(a, b, c) scanf("%lld %lld %lld", &a, &b, &c)
#define clong4(a, b, c, d) scanf("%lld %lld %lld %lld", &a, &b, &c, &d)
 
const long long MOD = 1000000007;
#define MODSET(d) if ((d) >= MOD) d %= MOD;
#define MODR(d) ((d)>=MOD?(d)%MOD:(d))
#define MODNEGSET(d) if ((d) < 0) d = ((d % MOD) + MOD) % MOD;
#define MODADDSET(d) if ((d) >= MOD) d -= MOD;
#define MODADDWHILESET(d) while ((d) >= MOD) d -= MOD;
 
#define foreach(it,c) for(__typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++) 
#define MAX 1000000
#define ll long long
#define mp make_pair
#define pb push_back
 
using namespace std;

ll negmod(ll number, ll mod)
{
    if(number >= 0) return number % mod;
    return (mod + (number % mod)) % mod;
}



// To compute (a * b) % mod
ll mulmod(ll a, ll b, ll mod)
{
    ll res = 0; // Initialize result
    a = a % mod;
    while (b > 0)
    {
        // If b is odd, add 'a' to result
        if (b % 2 == 1)
            res = (res + a) % mod;
 
        // Multiply 'a' with 2
        a = (a * 2) % mod;
 
        // Divide b by 2
        b /= 2;
    }
 
    // Return result
    return res % mod;
}
 
 
int main()
{
	#ifdef CHUCKIE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	
	int t;
	cin>>t;
	
	for(int q=0;q<t;q++)
	{
		
		ll n,k;
		cin>>n>>k;
		
		
		ll to=0,te=0,ro=0,re=0,l=0,r=0;
		if(k==1)
		{
			r=n/2;
			l= r*2!=n ? n/2 : n/2-1;
			if(l<0)l=0;
			cout<<"Case #"<<q+1<<": "<<r<<" "<<l<<endl;
			continue;
		}
		
		if(n%2==0)
		{
			to=1;
			te=1;
			if((n/2)%2==0)
			{
				re=n/2;ro=n/2-1;
			}
			else
			{
				re=n/2-1;ro=n/2;
			}
			
		}
		else
		{
			if((n/2)%2==0)
			{te=2;
			re=n/2;}
			
			else
			{
				to=2;
				ro=n/2;
			}
		}
		
		k--;
		//cout<<to<<" "<<ro<<" "<<te<<" "<<re<<endl;
		//cout<<k<<endl;
		ll to1=0,te1=0,ro1=0,re1=0,ansr=0;
		while(1)
		{
			to1=0,te1=0,ro1=0,re1=0;
			
			
			if(ro > re)
			{
				//if k lies in odd sections
				if(k <= to)
				{
					ansr=ro;
					break;
				}
				
				//fill odd sections
				k-=to;
				
				//if k lies in even sections
				if(k <=te )
				{
					ansr=re;
					break;	
				}
				k-=te;
			}
			
			
			if(ro < re)
			{
				//if k lies in even sections
				if(k <=te )
				{
					ansr=re;
					break;	
				}
				k-=te;
				
				//if k lies in odd sections
				if(k <= to)
				{
					ansr=ro;
					break;
				}
				
				//fill odd sections
				k-=to;
				
				
			}
			
			if(ro!=0){
				if((ro/2)%2==0)
				{
					re1=ro/2;
					te1=to*2;
				}
				else
				{
					ro1=ro/2;
					to1=to*2;
				}
			}
				
			if(re!=0){
				if((re/2)%2==0)
				{
					re1=re/2;
					ro1=re/2-1;
					if(ro1<0)ro1=0;
					te1+=te;
					to1+=te;
				}
				else
				{
					re1=re/2-1;
					if(re1<0)re1=0;
					ro1=re/2;
					te1+=te;
					to1+=te;
				}
			}
			
			
			
			to=to1;
			te=te1;
			ro=ro1;
			re=re1;
			//cout<<to<<" "<<ro<<" "<<te<<" "<<re<<endl;
			
			
		}
		
		
		r=ansr/2;
		l= r*2!=ansr ? ansr/2 : ansr/2-1;
		
		if(l<0)l=0;
		
		cout<<"Case #"<<q+1<<": "<<r<<" "<<l<<endl;
	}

	
	return 0;
}

