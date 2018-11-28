#include<bits/stdc++.h>
using namespace std;
int check(long int k){
	int pe=9;
	int r;
	while(k!=0){
		r=k%10;
		k=k/10;
		if(r>pe)
			return 0;
		pe=r;

	}
	return 1;
}
int main(){
	long int t;
	cin>>t;
	for(long int j=1;j<=t;j++){
		long int n;
		cin>>n;
		long int k;
		for(k=n;k>=1;k--){
			if(check(k))
				break;
		}
		cout<<"Case #"<<j<<": ";

		cout<<k<<endl;
	}
	return 0;
}
