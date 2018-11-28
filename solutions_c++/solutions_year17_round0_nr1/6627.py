
#include <bits/stdc++.h>
using namespace std;

#define fill(a,val) memset(a, (val), sizeof a)
#define pb push_back
#define lli long long int
#define scantype int
#define endl "\n"
#define unique(x) x.erase(unique(x.begin(),x.end()), x.end())

lli MOD  = 1000000007;
lli inf = 1e15;

void scan(scantype &x);
lli powermod(lli _a,lli _b,lli _m){lli _r=1;while(_b){if(_b%2==1)_r=(_r*_a)%_m;_b/=2;_a=(_a*_a)%_m;}return _r;}
lli string_to_number(string s){lli x=0; stringstream convert(s); convert>>x; return x;}
lli add(lli a,lli b){lli x = (a+b)%MOD; return x; }
lli mul(lli a,lli b){lli x = (a*b)%MOD; return x; }
lli sub(lli a,lli b){lli x = (a-b+MOD)%MOD; return x; }
lli divi(lli a,lli b){lli x = a;lli y = powermod(b,MOD-2,MOD);lli res = (x*y)%MOD;return res;}

#define N 100003

int main(void)
{
  int t;
  cin>>t;

  for(int test=1;test<=t;test++)
  {
  	string st;
  	int k;
  	cin>>st>>k;


  	int minus = 0,n = st.length();
  	int dp[n+2];

  	fill(dp,0);

  	int res = 0 , flip = 0;
  	for(int l=0,r=k-1;r<n;l++,r++)
  	{
  		flip += dp[l];

  		if( (st[l]=='-' && flip%2==0) | (st[l]=='+' && flip%2) ) 
  		{
  			flip++;
  			res++;
  			dp[r+1]--;
  		}
  	}

  	bool possible = true;

  	for(int i=n-k+1;i<n;i++)
  	{
  		flip += dp[i];
  		if( (st[i]=='-' && flip%2==0) | (st[i]=='+' && flip%2) )
  			possible = false; 
  	}

  	if(possible)
  		printf("Case #%d: %d\n",test,res);
  	else
  		printf("Case #%d: Impossible\n",test);
  }
  return 0;
}


void scan(scantype &x)
{
    register int c = getchar(); //for negative/positive
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = getchar());
    if(c=='-') {neg=1;c=getchar();}
    for(;c>47 && c<58;c = getchar()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

