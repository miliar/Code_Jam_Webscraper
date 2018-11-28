
#include <bitset>
#include <string>
#include <iostream>
#include <climits>
#include <fstream>


using namespace std;


int flipPancake(string S, int K) {
	int n = S.size();
	bitset<1000> b(S, 0, n, '-', '+');
	// cout << b << endl;
	
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		// cout << b[i] << endl;
		// b.set(i, b[i] ^ 1);
		if (b[i] == 0) {
			++cnt;
			if (i + K < n) {
				for (int j = 0; j < K; ++j) {
					b.flip(i + j);
				}
			} else {
				for (int j = n - 1; j >= n - K; --j) {
					b.flip(j);
				}
			}
		}
		// cout << b << endl;
		if (b.count() == n) break;
	}
	// cout << b << endl;
	return (b.count() == n) ? cnt : -1;
}


int main() {
	
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	int n, K;
	in >> n;
	string S;
	
	for (int i = 1; i <= n; ++i) {
		in >> S >> K;
		out << "Case #" << i << ": ";
		int res = flipPancake(S, K);
		if (res == -1) out << "IMPOSSIBLE" << endl;
		else out << res << endl;
	}
	
	// cout << flipPancake("---+-++-", 3) << endl;
	// cout << flipPancake("+++++", 4) << endl;
	// cout << flipPancake("-+-+-", 4) << endl;
	// cout << flipPancake("-++-+---", 3) << endl;
}
