#include<iostream>
#include<string>
using namespace std;

bool tidyN(long long n){
	int num = 9;
	for (int i = 0; i < 32; i++){
		if (n%10 <= num){
			num = n%10;
			n = n/10;
		} else {
			return false;
		}
	}

	return true;
}

long long lastTidy(long long n){
	while (!tidyN(n)){
		n--;
	}

	return n;
}

int main(void){
	int T = 0;
	long long N = 0;

	cin >> T;
	if (1 > T || T > 100) return 0;
	for (int i = 0; i < T; i++){
		cin >> N;
		if (1 > N || N > 1000) continue; /*small dataset*/
		
		cout << "Case #" << (i+1) << ": " << lastTidy(N) << "\n";
	}

	return 0;
}
