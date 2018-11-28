#include <bits/stdc++.h>

using namespace std;
 
unsigned long long k, n;

bool dig_check(unsigned long long n){
	unsigned long long dig = 9;
	while (n != 0){
		if (dig < n%10){
			return false;
		}
		dig = n%10;
		n/=10;
	}
	if (n == 0){
		return true;
	}
}

unsigned long long digify(unsigned long long n){
	vector<unsigned long long> digits;
	unsigned long long ans = 0;
	digits.clear();
	while (n != 0){
		digits.push_back(n%10);
		n/=10;
	}
	unsigned long long nte = 0;
	bool stat = false;
	for (int i = digits.size()-1; i >= 0; i--){
		if (!stat && digits[i] >= digits[i-1]){
			nte = digits[i];
			ans += nte-1;
			ans*=10;
			stat = true;
			continue;
		}
		else if (!stat){
			ans += digits[i];
			ans*=10;
		}
		else if (stat){
			ans+=9;
			ans*=10;
		}
	}
	return ans/10;
}

int main(){
	cin >> k;
	for (int i = 1; i <= k; i++){
		cin >> n;
		if (dig_check(n)){
			cout << "Case #" << i << ": " << n << endl;
		}
		else {
			digify(n);
			cout << "Case #" << i << ": " << digify(n) << endl;
		}
	}
}