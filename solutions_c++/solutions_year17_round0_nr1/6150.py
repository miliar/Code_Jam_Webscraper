#include <iostream>
#include <string.h>
using namespace std;


void solve(int t){
	int n,k;
	char s[1005];
	int x[1005],y[1005];
	cin>>s>>k;
	n=strlen(s);
	// cout<<s<<endl;
	for(int i=0;i<n;i++){
		y[i]=0;
		if(s[i]=='-')
		x[i]=0;
		else
		x[i]=1;
	}
	y[n]=0;
	
	long long int ans=0;
	for(int i=0;i<n;i++) {
		if(i < n-k+1 && (x[i]+y[i])%2 ==0) {
			ans++;
			y[i]++;
			y[i+k]--;
		}
		y[i+1]+=y[i];
		// cout<<x[i]<<y[i]<<endl;
	}
	cout<<"Case #"<<t<<": ";
	for(int i=0;i<n;i++) {
		if( (x[i]+y[i])%2==0 ){
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
	}
	cout<<ans<<endl;
}

int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		solve(i+1);
	}
	return 0;
}