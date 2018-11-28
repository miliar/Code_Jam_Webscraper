#include <iostream>
#include <vector>
using namespace std;

bool isTidy(long long num) {
	while(num != 0) {
		int k = num%10;
		num /= 10;
		if (k < num%10)
			return false;
	}
	
	return true;
}

int main() {
	int cas;
	cin >> cas;
	for (int c = 1; c <= cas; c++) {
		long long num;
		cin >> num;
		
		for (long long i = num; i >= 0; i--) {
			if (isTidy(i)) {
				cout << "Case #" << c << ": "<<i<<endl;
				break;
			}
		}
	}
		
}