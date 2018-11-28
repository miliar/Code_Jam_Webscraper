#include <iostream>
using namespace std;

bool isSorted(long long n){
	long long next = n %10;
	long long cur;
	while(n > 9){
		cur = next;
		n = n/10;
		next = n % 10;
		if(cur < next)
			return false;
	}

	return true;
}

int main(){
	int t;
	cin>>t;

	for(int j = 1; j <= t; j++){
		int n;
		cin>>n;
		
		for(long long i = n; i >=1; i--){
			if(isSorted(i)){
				cout<<"Case #"<<j<<": "<<i<<endl;
				break;
			}
			
		}
	}
}