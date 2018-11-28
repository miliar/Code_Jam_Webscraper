#include <bits/stdc++.h>

using namespace std;

bool checkTidy(unsigned long long n){
	int a, b;
	b = n%10;
	n /= 10;
	while(n > 0){
		a = n%10;
		if(a > b) return false;
		b = a;
		n /= 10;
	}
	return true;
}


int main(){
	int rep;
	cin >> rep;
	for(int _rep = 0; _rep < rep; _rep++){
		unsigned long long n;
		scanf("%lld",&n);
		//cout << "li\n";
		while(!checkTidy(n)){
			n--;
		}
		printf("Case #%d: %lld\n", _rep+1, n);
	}
}