#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#define forr(i,a,b) for(int i=(a);(i)<int(b);(i)++)
#define forn(i,n) forr(i,0,n)
#define pb push_back

using namespace std;

typedef unsigned long long ull;
typedef long long ll;


ll make_tidy (ll n){
	vector <int> v;
	
	while(n){
		v.pb(n%10);
		n/=10;
	}
	
	
	int smallest=9;
	forn(i, v.size()){
		if(v[i]>smallest){
			v[i]--;
			forn(j,i)
				v[j]=9;
			smallest = v[i];
		}
		
		smallest = min(smallest, v[i]);
	}
	
	reverse(v.begin(),v.end());
	
	forn(i,v.size()){
		n*=10;
		n+=v[i];
	}
	
	return n;
}

int main(){
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	ll t,n;
	
	cin>>t;
	
	forn(testc,t){
		cin>>n;
		
		
		cout<<"Case #"<<testc+1<<": "<<make_tidy(n)<<"\n";
	}
	
	return 0;
}
