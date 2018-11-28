#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <queue>

#include <math.h>
#include <set>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long
#define ull unsigned long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;

int n;
vector<ll> ft;

ll gcd(ll a, ll b) {
	if(!b)
		return a;
	return a%b? gcd(b,a%b):b;
}

ll t_gcd(ll a, ll b) {
	if(a<0) {
		a = -a;
	}
	if(b<0) {
		b = -b;
	}

	if(a<b)
		swap(a,b);

	//printf("a = %lld b = %lld\n",a,b);

	ll ret = gcd(a,b);
	//printf("a = %lld b = %lld ret = %lld\n",a,b,ret);
	return ret;
}

int solve() {
	int ans = 0;
	for(int i = 0; i + 1 < n; ++i) {
		while(t_gcd(ft[i],ft[i+1])==1) {
			ll t1 = ft[i];
			ll t2 = ft[i+1];
			ft[i] = t1 - t2;
			ft[i+1] = t1 + t2;
			ans++;
		}
	}
	return ans;
}

int main()
{
	int T;
	cin>>T;
	fr(ca,0,T) {
		ll d;
		int n;
		cin>>d>>n;
		double max_time = 0;
		fr(i,0,n) {
			ll k,s;
			cin>>k>>s;
			double time = (double)(d-k)/s;
			max_time = max(time, max_time);
		}
		printf("Case #%d: %.7lf\n",ca+1,d/max_time);
	}
}
