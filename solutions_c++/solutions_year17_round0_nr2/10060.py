#include <iostream>
#include <string>
using namespace std;

int getDigits(long long n){
	int result = 0;
	while(n > 0){
		n /= 10;
		result ++;
	}
	return result;
}

int pow(int x, int p){
  if (p == 0) return 1;
  if (p == 1) return x;

  int tmp = pow(x, p/2);
  if (p%2 == 0) return tmp * tmp;
  else return x * tmp * tmp;
}

long long solve(long long n){
	int digits = getDigits(n);

	for(int i = 0; i<digits; i++){
		int prev = n/pow(10, digits - i)%10;
		int current = n/pow(10, digits - i - 1)%10;
		if(prev > current){
			n = n/pow(10, digits - i)*pow(10, digits - i) - 1;
			i = 0;
		}
	}
	return n;
}

int main(){
	int t;
	string s;
	cin >> t;
	for(int i = 0; i<t; i++){
		long long n;
		cin>>n;
		long long result = solve(n);
		cout<<"Case #"<<(i+1)<<": "<<result<<endl;

	}
}