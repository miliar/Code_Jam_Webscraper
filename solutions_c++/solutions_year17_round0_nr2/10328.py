#include<iostream>
using namespace std;

bool isTiny(long  unsigned int N) {
	bool isTiny = true;
	long unsigned int num = 9;
	while (N/10 > 0) {
		//cout << "N/10 " << N / 10 << "  " << N % 10 << endl;
		if (N % 10 > num) isTiny = false;
		num = N % 10; N /= 10;
	}
	if (N % 10 > num) isTiny = false;
	num = N % 10; N /= 10;
	//cout << "N/10 " << N / 10 << "  " << N % 10 << endl;
	return isTiny;
}

int main() {
	int T, i;
	long unsigned int N;
	bool found;
	cin >> T;
	i = T;
	while (i--) {
		cin >> N;
		found = false;
		while (!found) {
			if (isTiny(N)) found = true;
			else N--;
		}
		cout << "Case #" << T - i << ": " << N << endl;
	}
	return 0;
}