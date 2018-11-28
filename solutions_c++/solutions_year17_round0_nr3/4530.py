#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		ll n,k;
		cin>>n>>k;
		priority_queue<ll,vector<ll> > p;
		p.push(n);
		for(int i=1;i<k;i++){
			ll m = p.top();
			p.pop();
			p.push(m/2);
			p.push((m-1)/2);
		}
		cout<<"Case #"<<l<<": "<<(p.top())/2<<" "<<(p.top()-1)/2<<"\n";
	}
}
