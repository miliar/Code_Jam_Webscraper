#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		long long N, K;
		cin >> N >> K;

		N++;
		long long k = 1;
		while (2*k <= K) k *= 2;
		long long small = N/k;
		long long nbig = N-k*small;

		long long size = small+(K-k < nbig ? 1 : 0);
		cout << "Case #" << t << ": " << (size+1)/2-1 << ' ' << size/2-1 << '\n';
	}

	return 0;
}
