/*input
5
4 2
5 2
6 2
1000 1000
1000 1


*/
#include "bits/stdc++.h" 
using namespace std;
#define ll long long

int main(int argc, char const *argv[]){
	ll T,n,k;
	ios::sync_with_stdio(0)	;
	cin>>T;
	for(ll cases=1;cases<=T;cases++){
		cin>>n>>k;
		cout<<"Case #"<<cases<<": ";
		priority_queue<ll> parts;
		parts.push(n);
		for(ll i=0;i<k-1;i++){
			ll sz = parts.top(); parts.pop();
			parts.push(sz/2);parts.push(sz - sz/2 - 1 );
		}
		ll sz = parts.top(); parts.pop();
		cout<<sz/2<<' ' <<sz - sz/2 -1<<'\n';		
	}
}
