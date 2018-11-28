#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
using namespace std;


int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	ll t,k,n,i=1;
	ifstream infile;
	ofstream outfile;
	infile.open("C-small-2-attempt0.in");
	outfile.open("output.txt");
	infile>>t;
	while(t--){
		infile>>n>>k;
		priority_queue<ll>q;
		q.push(n);
		for(ll j=0;j<k-1;j++){
			ll a=q.top();
			q.pop();
			if(a%2==0){ q.push(a/2);q.push(a/2-1);}
			else{ q.push(a/2);q.push(a/2);}
		}
		ll a=q.top();
		ll ans1=a/2;
		ll ans2=a-ans1-1;
		outfile<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;
		
		i++;
	}
	return 0;
}
