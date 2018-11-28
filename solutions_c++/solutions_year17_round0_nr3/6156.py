/*****************************************************************************************
You should enjoy the little detours...
Becase that's where you'll find the things
more important than what you want...

Version	:	1.5
Author	:	Harshwardhan Praveen
*****************************************************************************************/
#include <bits/stdc++.h>
using namespace std;

#define pi 			3.141592653593
#define MIN 		-1000000001
#define MAX 		1000000001
#define EPS 		0.000000001

#define cns 		ios_base::sync_with_stdio(false)
#define DEBUG(x) 	cout << '>' << #x << ':' << x << endl
#define REP(i,n) 	for(ll i=0;i<(n);i++)
#define FOR(i,a,b) 	for(ll i=(a);i<(b);i++)
#define DFOR(i,a,b) for(ll i=(a);i>(b);i--)
#define pb 			push_back
#define mp 			make_pair
#define all(v) 		v.begin(),v.end()
#define rall(v) 	v.rbegin(),v.rend()
#define vi 			vector<int>
#define vl 			vector<ll>
#define vii 		vector<vector<int> >
#define vll 		vector<vector<ll> >
#define vs 			vector<string>
#define si 			set<int>
#define pii 		pair<int,int>
#define pll			pair<ll,ll>
#define F 			first
#define S 			second
#define ll 			long long
#define ull 		unsigned long long

ll power_modulo(ll base, ll exp, ll mod){
	ll result = 1;
	base %= mod;
	while(exp > 0){
		if(exp%2 == 1)
			result = (result*base) % mod;
		exp = exp>>1;
		base = (base*base) % mod;
	}
	return result;
}

int main(){
	ll t,n,k;
	cin>>t;
	FOR(i,1,t+1){
		cin>>n>>k;
		ll power=0;
		while(pow(2,power)<k+1)
			power++;
		power--;
		ll modd = (ll)pow(2,power);
		ll L2 = n/modd;
		ll L1 = L2 -1 ;
/*		
		DEBUG(modd);
		DEBUG(L1);
		DEBUG(L2);
*/
		ll available = n - modd + 1;
		ll num;
		num = available - (modd*L1); 
		ll diff = k - modd + 1, split;
/*
		DEBUG(available);
		DEBUG(num);
		DEBUG(diff);
*/
		if(diff<=num)
			split = L2;
		else
			split = L1;
		if(split%2==1)
			cout<<"Case #"<<i<<": "<<split/2 <<" "<< split/2;
		else
			cout<<"Case #"<<i<<": "<<split/2 <<" "<< split/2 - 1;
		cout<<endl;
	}
}