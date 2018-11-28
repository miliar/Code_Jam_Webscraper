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
	int t;
	cin>>t;
	FOR(i,1,t+1){
		string s;
		cin>>s;
		bool flag=true;
		REP(j,s.size()-1)
			if(s[j]>s[j+1]){
				flag=false;
				break;
			}
		if(flag){
			cout<<"Case #"<<i<<": "<<s<<endl;
			continue;
		}
		int j=0;
		while(s[j+1]>s[j])
			j++;
		while(s[j]==s[j-1])
			j--;
		s[j]-=1;
		FOR(k,j+1,s.size())
			s[k]='0'+9;
		cout<<"Case #"<<i<<": ";
		int k=0;
		while(s[k] == '0')
			k++;
		while(k<s.size()){
			cout<<s[k++];
		}
		cout<<endl;
	}		
}
