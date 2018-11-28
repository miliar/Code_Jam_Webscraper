#include <iostream>
using namespace std;


int main() {
	int t,same = 0,sameNum = -1,b = 0;
	long long int num, num1;
	cin >> t;
	for (int p = 1; p <= t; p++) {
		cin >> num;
		num1 = num;
		while (num1 > 0) {
			b++;
			num1 /= 10;
		}
		for (int i = 0; i < b - 1; i++) {
			int n1 = num / (long long)pow(10, b - 1 - i) % 10, n2 = num / (long long)pow(10, b - 2 - i) % 10;
			if (n1 > n2) {
				num -= (long long)pow(10, b + same - 1 - i);
				num = num / (long long)pow(10, b + same - 1 - i) * (long long)pow(10, b + same - 1 - i);
				for (int j = 0; j < b + same - 1 - i;j++) {
					num += 9*(long long)pow(10, j);
				}
				break;
				//change
			}
			else if (n1 == n2) {
				same++;
			}
			else {
				sameNum = n2;
				same = 0;

			}
		}
		cout << "Case #" << p << ": " << num << endl;
	}
	return 0;
}