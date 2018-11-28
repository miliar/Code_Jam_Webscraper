#include <iostream>

using namespace std;

bool isTidy(int n) {
	int prev = 9;
	while (n) {
		if (n % 10 > prev) return false;
		prev = n % 10;
		n /= 10;
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	for (int q = 1; q <= T; ++q) {
		int N;
		cin >> N;
		int ret = 1;
		for (int i = 2; i <= N; ++i) if (isTidy(i)) ret = i;
		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}