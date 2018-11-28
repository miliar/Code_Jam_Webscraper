#include <iostream>
#include <string.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		char num[25];
		cin >> num;
		for (int j = strlen(num) - 2; j >= 0; j--) {
			if (num[j] > num[j+1]) {
				for (int k = j+1; k < strlen(num); k++)
					num[k] = '9';
				num[j]--;
			}
		}
		for (int j = 0; j < strlen(num); j++) {
			if (num[j] != '0')
				break;
			for (int k = 0; k < strlen(num); k++) {
				num[k] = num[k+1];
			}
		}
		cout << "Case #" << i+1 << ": " << num << endl;
	}
	return 0;
}
