#include<iostream>

using namespace std;

bool tidy(int n){

	int l = 10;
	while(n>0){

		if(l<n%10)
			return false;
		l = n%10;
		n/=10;

	}
	return true;

}

int main(int argc, char **argv) {

	ios::sync_with_stdio(false);
	int n;
	int t;
	cin>>t;

	for(int j=1;j<=t;j++){
		cin>>n;
		for(int i=n;i>0;i--){
			if(tidy(i)){
				cout<<"Case #"<<j<<": "<<i<<endl;
				break;
			}
		}
	}

	return 0;

}
