#include <iostream>
using namespace std;
int main() {
	int num = 0;
	int numb = 0;
	cin >> num;
	int digits = 0;
	int sam = 1;
	int temp = 0;
	int temp1 = 1;
	int temp2 = 0;
	int arr[num];
	bool low;
	for (int a = 0; a < num; a++) {
		cin >> numb;
		temp2 = numb;
		while (temp2 > 0) {
			temp2 /= 10;
			digits++;
		}
		
		for (int b = 1; b < digits; b++) {
			sam *= 10;
		}
		
		for (int c = 1; c <= sam; c *= 10) {
			low = true;
			while (low) {
				temp = (numb / c) % 10;
				temp1 = (numb / (c * 10)) % 10;
				if (temp <temp1) {
					numb--;
				}
				else {
					low = false;
				}
			}
		}
		low = true;
		arr[a] = numb;
		numb = 0;
		digits=0;
		sam=1;
	}
	for (int d = 0; d < num; d++) {
		cout << "Case #" << d + 1 << ": " << arr[d] << endl;
	}
	return 0;
}
