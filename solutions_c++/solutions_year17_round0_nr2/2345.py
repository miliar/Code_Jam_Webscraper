#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int T;
long long N, k;

bool isIncreasing(long long a){
	if(a>9){
		long long p;
		while(a){
			p = a%10;
			a /= 10;
			if((a%10)>p) return false;
		}
	}
	return true;
}

long long getInc(long long n){
	k = 0;
	while(!isIncreasing(n)){
		k++;
		n /= 10;
	}
	if(k){
		long long d = n%10;
		n = n/10;
		while((n%10)==d){
			k++;
			n /= 10;
		}
		n = 10*n+d;
		n--;
		for(int i=0; i<k; i++){
			n = 10*n+9;
		}
	}
	return n;
}

int main(){
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> N;
		cout << "Case #" << t << ": " << getInc(N) << "\n";
	}
	return 0;
}
