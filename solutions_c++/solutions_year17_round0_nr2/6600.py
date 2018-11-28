
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
  	cin>>st;

  	int n = st.length();

  	for(int cnt=0;cnt<n;cnt++){
  		for(int i=n-2;i>=0;i--)
  		{
  			if(st[i]>st[i+1])
  			{
  				st[i]--;
  				for(int j=i+1;j<n;j++)
  					st[j] = '9';
  				break;
  			}
  		}
  	}
  	string res;

  	for(int i=0;i<st.length();i++)
  		if(st[i]!='0')
  		{
  			for(int j=i;j<st.length();j++)
  				res+=st[j];
  			break;
  		}
  	cout<<"Case #"<<test<<": "<<res<<endl;
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

