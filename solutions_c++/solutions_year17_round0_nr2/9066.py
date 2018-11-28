#include <iostream>
#include <set>
#include <math.h>
using namespace std;

bool checktidy(long long N) {
	int init = N % 10;
	while (N) {
		N = N / 10;
		if (init >= (N % 10)) {
			init = N % 10;
		}
		else {
			return false;
		}
	}
	return true;
}
int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		long long N;
		cin >> N;
		for (long long j = N; j > 0; --j) {
			if (checktidy(j) == true) {
				cout << "Case #" << i << ": " << j << endl;
				j = 0;
			}
		}
		

	}

	//cin.get();
	//cin.get();
	return 0;
}
