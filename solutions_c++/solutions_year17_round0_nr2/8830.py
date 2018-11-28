#include <iostream>
using namespace std;

bool test(long long unsigned a){
	long long unsigned b = a;
	unsigned int last_digit = b%10;
	while (b != 0){
		b = b/10;
		if (b%10 > last_digit) {return false;}
		last_digit = b%10;
	}
	return true;
}



long long unsigned foo(long long unsigned n){
	for (long long unsigned i = n; i != 0; i -= 1){
		if (test(i)) return i;
	}
	return 0;	
}

int main(void){
	const bool debug = false;
	if (not debug){
		int t = 0;
		cin >> t;
		for (int i = 1; i <= t; i += 1){
			long long unsigned n = 0;
			cin >> n;
			cout << "Case #" << i << ": " << foo(n) << endl;
		}
	} else {
		cout << bool(foo(132) == 129) << endl;
		cout << bool(foo(1000) == 999) << endl;
		cout << bool(foo(7) == 7) << endl;
	}
}

