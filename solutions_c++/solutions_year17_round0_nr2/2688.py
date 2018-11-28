#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int a[20];

int main() {
	int T;
	long long int n;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int length = 0;
		long long int tmp = 0;
		cin >> n;
		long long int tmp2 = n;
		while (n != 0) {
			a[length++] = n % 10;
			n /= 10;
			tmp = tmp * 10 + 1;
		}
		if (tmp2 < tmp) {
			cout << "Case #" << i + 1 << ": ";
			for (int j = 0; j < length - 1; j++) cout << 9;
			cout << endl;
		}
		else {
			while (true) {
				bool b = true;
				for (int j = length - 1; j > 0; j--) {
					if (a[j] > a[j - 1]) {
						a[j - 1] = 9;
						a[j]--;
						for (int k = j - 2; k >= 0; k--) a[k] = 9;
						b = false;
						break;
					}
				}
				if (b) break;
			}
			
			cout << "Case #" << i + 1 << ": ";
			for (int j = length - 1; j >= 0; j--) cout << a[j];
			cout << endl;
		}
	}
}