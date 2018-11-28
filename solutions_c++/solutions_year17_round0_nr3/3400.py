#include <bits/stdc++.h>

#define lli long long int
#define llu unsigned long long int
#define rep(i,x,m) for(int i=x; i<m; i++)
#define replli(i,x,m) for(lli i=x; i<m; i++)
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d",n);
#define slli(n) scanf("%lld",&n);
#define plli(n) printf("%lld",n);
#define ss(n) scanf("%s",n);
#define ps(n) printf("%s",n);
#define br printf("\n");
#define MOD 1000000007
#define INF 9223372036854775807;
#define output lli
#define v(a) vector< a >
#define vp(a,b) vector< pair< a, b > >

using namespace std;

void printOp(int i, output o1, output o2) {printf("Case #%d: %lld %lld\n",i,o1,o2);}
lli add(lli a,lli b,lli m=MOD){lli x=a+b;while(x>=m)x-=m;return x;}
lli sub(lli a,lli b,lli m=MOD){lli x=a-b;while(x<0)x+=m;return x;}
lli mul(lli a,lli b,lli m=MOD){lli x=a*b;x%=m;return x;}
lli powermod(lli _a,lli _b,lli _m){lli _r=1;while(_b){if(_b%2==1)_r=(_r*_a)%_m;_b/=2;_a=(_a*_a)%_m;}return _r;}
lli mid(lli a, lli b){return (a+b)/2;}
lli div(lli a, lli b, lli m=MOD){return mul(a,powermod(b,m-2,m));}
lli nCr(lli n, lli r){if(r > n / 2) r = n - r;lli ans = 1;lli i;for(i = 1; i <= r; i++){ans *= n - r + i;ans /= i;}return ans;}

output actualFuncSmall(output &o2)
{
	lli n,k;
	slli(n);
	slli(k);

	priority_queue<lli> q;
	q.push(n);

	replli(i,0,k-1)
	{
		lli t = q.top();
		q.pop();
		if (t%2)
		{
			q.push(t/2);
			q.push(t/2);
		}
		else
		{
			q.push(t/2);
			q.push((t/2)-1);
		}
	}
	lli t = q.top();
	o2 = t/2;
	if(t%2 == 0)
		o2 = o2-1;
	return t/2;
}

int main()
{
	int t;
	si(t);
	rep(i,0,t)
	{
		lli o2 = 0;
		output o1 = actualFuncSmall(o2);
		printOp(i+1,o1,o2);
	}
	return 0;
}