#include <iostream>
using namespace std;


bool isTidy(long n){
	bool tidy = false;
	int lastDigit = 10;
	while(n > 0){
		int digit = n%10;
		if(digit <= lastDigit){
			tidy = true;
			lastDigit = digit;
		}
		else return false;
		n /= 10;		
	}
	return tidy;
}

int main(){
	int T;
	cin >> T;
	for(int iT = 0; iT < T; iT++){
		long ans;
		long n;
		cin >> n;
		ans = n;
		while(!isTidy(ans)) ans--;

		cout << "Case #" << iT+1 << ": " << ans << endl;
	}
	return 0;
}
