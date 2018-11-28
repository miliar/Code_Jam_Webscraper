
#include <bits/stdc++.h>
using namespace std;

#define fill(a,val) memset(a, (val), sizeof a)
#define pb push_back
#define lli long long int
#define scantype long long int
#define endl "\n"
#define unique(x) x.erase(unique(x.begin(),x.end()), x.end())

lli MOD  = 1000000007;
lli inf = 1e15;
double eps = 0.0000001;

void scan(scantype &x);
lli powermod(lli _a,lli _b,lli _m){lli _r=1;while(_b){if(_b%2==1)_r=(_r*_a)%_m;_b/=2;_a=(_a*_a)%_m;}return _r;}
lli string_to_number(string s){lli x=0; stringstream convert(s); convert>>x; return x;}
lli add(lli a,lli b){lli x = (a+b)%MOD; return x; }
lli mul(lli a,lli b){lli x = (a*b)%MOD; return x; }
lli sub(lli a,lli b){lli x = (a-b+MOD)%MOD; return x; }
lli divi(lli a,lli b){lli x = a;lli y = powermod(b,MOD-2,MOD);lli res = (x*y)%MOD;return res;}

#define N 100003

void solve(int testcase)
{
	double d;
	int n;
	cin>>d>>n;

	lli pos[n],speed[n];

	for(int i=1;i<=n;i++)
	{
		int x,y;
		scan(pos[i]);
		scan(speed[i]);
	}

	int low_idx = 0 , last = 1e9 + 4;

	double timeR = 0;

	for(int i=1;i<=n;i++)
	{
		double tmp = (d - pos[i]) / (double) speed[i];
		timeR = max(timeR , tmp);
	}

	double res = d / timeR;

	printf("Case #%d: %.9f\n",testcase,res);
}
int main(void)
{
  int t;
  cin>>t;

  for(int i=1;i<=t;i++)
	  solve(i);

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

