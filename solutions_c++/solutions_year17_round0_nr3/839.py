#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mkp make_pair
#define bgn begin()
#define end end()
#define all(x) x.bgn,x.end
#define itr(x) x::iterator
#define fst first
#define scd second
#define dlt pop()

using namespace std;

typedef long long int ll;
typedef vector<int> vint;
typedef vector<ll> vlong;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef map<int,int> mii;
typedef map<ll,ll> mll;
typedef queue<int> qint;
typedef queue<ll> qlong;
typedef stack<int> sint;
typedef stack<ll> slong;
typedef queue<pii> qpii;
typedef stack<pii> spii;

int mod = 1e9+7;
int NN = 1e6+7;

ll gcd(ll a, ll b){
	return b==0 ? a : gcd(b,a%b);
}

// (1/b)%a where gcd(a,b)=1
ll invmod(ll a, ll b){
	ll x=0, y=1, r, q, m=a;
	while(b){
		r=a%b;
		q=a/b;
		a=b;
		b=r;
		r=x;
		x=y;
		y=r-q*y;
	}
	return (x+m)%m;
}

pll sol(ll n, ll k){
	ll cnt1=1, cnt2=0;
	while(k>0 && n>0){
		if(k<=cnt1){
			if(n%2) return mkp(n/2,n/2);
			return mkp(n/2,n/2-1);
		}
		k-=cnt1;
		if(k<=cnt2){
			if((n-1)%2) return mkp((n-1)/2,(n-1)/2);
			return mkp((n-1)/2,(n-1)/2-1);	
		}
		k-=cnt2;
		if(n&1) cnt1=cnt1+cnt1+cnt2;
		else cnt2=cnt2+cnt2+cnt1; 
		n/=2;
	}

	// function control should not reach this point
	if(n%2) return mkp(n/2,n/2);
	return mkp(n/2,n/2-1);
}

int main(){
	int t;
	cin>>t;
	for(int z=1; z<=t; z++){
		ll n, k;
		cin>>n>>k;
		pll ans=sol(n,k);
		cout<<"Case #"<<z<<": "<<ans.fst<<" "<<ans.scd<<endl;
	}
}