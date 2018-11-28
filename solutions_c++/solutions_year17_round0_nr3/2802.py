#include <iostream>

using namespace std;

typedef unsigned long long ull;

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		ull n,k; cin>>n>>k;
		while(k>1){
			if(n%2==0 && k%2==0) n/=2;
			else n=(n-1)/2;
			k/=2;
		}
		cout<<"Case #"<<t<<": ";
		if(n==0) cout<<"0 0"<<endl;
		else cout<<(n/2)<<' '<<((n-1)/2)<<endl;
	}
	return 0;
}