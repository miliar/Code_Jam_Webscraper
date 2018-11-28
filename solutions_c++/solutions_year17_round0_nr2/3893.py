#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
using namespace std;
ll fun(ll n){
	ll a[50],i=0,j,k,ans=0,l=0;
	while(n>0){
		a[i++]=n%10;
		n=n/10;
	}
	k=i-1;
	for(j=i-1;j>0;j--){
		if(a[j]<a[j-1]) k=j-1;
		else if(a[j]>a[j-1]) {l=1;break;}
	}
	if(l==1){for(j=0;j<k;j++) a[j]=9;
	 a[k]=a[k]-1;}
	for(j=i-1;j>=0;j--) ans=ans*10+a[j];
	return ans;
}

int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	ll t,n,i=1;
	ifstream infile;
	ofstream outfile;
	infile.open("B-large.in");
	outfile.open("output.txt");
	infile>>t;
	while(t--){
		infile>>n;
		ll ans=fun(n);
		outfile<<"Case #"<<i<<": "<<ans<<endl;
		i++;
	}
	return 0;
}
