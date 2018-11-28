#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
using namespace std;
ll fun(string s,ll k){
ll ans=0,minus=0,j,l;
	ll n=s.size();
	for(j=0;j<=n-k;j++){
		if(s[j]=='-'){
			ans++;
			for(l=j;l<j+k;l++){
				if(s[l]=='-') s[l]='+';
				else s[l]='-';
			}
		}
	}
				
	minus=0;
	for(j=0;j<n;j++) if(s[j]=='-') minus++;	
	if(minus==0) return ans;
	else return -1;
}

int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	ll t,k,i=1;
	string s;
	ifstream infile;
	ofstream outfile;
	infile.open("A-large.in");
	outfile.open("output.txt");
	infile>>t;
	while(t--){
		infile>>s>>k;
		ll ans=fun(s,k);
		if(ans>=0) outfile<<"Case #"<<i<<": "<<ans<<endl;
		else outfile<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		i++;
	}
	return 0;
}
