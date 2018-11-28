#include <iostream>
using namespace std;

bool checkTidy(long long n){
	while(n>0){
		long long a = (n/10)%10;
		long long b = n%10;
		if(b<a){
			return false;
		}
		n=n/10;
	}
	return true;
}

int main() {
	int T;
	long long N;
	long long last;

	cin>>T;

	for(int i=0;i<T;i++){
		cin>>N;
		for(long long j=N;j>0;j--){
			if(checkTidy(j)){
				cout<< "Case #"<<i+1<<": "<<j<<endl;
				break;
			}
		}
	}
	return 0;
}
