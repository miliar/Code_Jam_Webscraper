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
		string s;
		cin>>s;
		int p=-1,flag=0;
		for(int i=1;i<s.length();i++)
		{
				if(s[i]>=s[i-1])
				{
					continue;
				}
				
				flag=1;
				for(int j=i-1;j>=0;j--)
				{
					if(s[j]!=s[i-1])
					{
						p=j;
					}
				}
				break;
		}
		if(flag==1){
		p++;
		
		s[p]=s[p]-1;
		for(int j=p+1;j<s.length();j++)s[j]='9';
		
		if(s[0]=='0')s=s.substr(1,s.length()-1);}
		
		cout<<"Case #"<<q+1<<": "<<s<<endl;
	}

	
	return 0;
}

