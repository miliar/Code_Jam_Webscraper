//template by chamow
#include<bits/stdc++.h>
#include <limits>
/*-------------------------------------------------------- */
using namespace std;

/*-------------------------------------------------------- */

#define rep(i,val,n) for(ll i=val;i<n;i++)
#define per(j,val,n) for(ll j=val;j>=n;j--)
#define pb push_back
#define pi 3.14157
#define mp make_pair
#define MODULO 1000000007
#define INF 1000000000000000

/*-------------------------------------------------------- */

typedef long long ll;
typedef vector<bool> boolean;
typedef vector<ll> vec;


/*-------------------------------------------------------- */

ll gcd(ll a, ll b)
{
	if(b == 0)
	{
		return a;
	}
	return gcd(b, a%b);
}

ll lcm(ll a, ll b)
{
	return ((a*b)/gcd(a,b));
}

long long int read_int(){
	char r;
	bool start=false,neg=false;
	long long int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}
/*-------------------------------------------------------- */
bool myFunc(vector<double> &a, vector<double> &b)
{
    return a > b;
}

int main()
{
    ll t, d, n, k, s, l = 0;
    cin>>t;
    while(t--)
    {
        l++;
        cin>>d>>n;
        vector<long double> v;
        rep(i,0,n)
        {
            cin>>k>>s;
            long double val = double((d - k)*(1.0000000000000)/(s)*(1.000000000000));
            v.pb(val);
        }
        sort(v.begin(), v.end());
        long double temp = v[n-1] * 1.0000000000000000;
        long double ans = (d*1.000000)/(temp*1.000);
        cout<<"Case #"<<l<<": "<<setprecision(10)<<ans<<endl;
    }
	return 0;
}