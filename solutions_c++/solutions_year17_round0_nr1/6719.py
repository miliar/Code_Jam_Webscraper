#include <bits/stdc++.h>
using namespace std;

void test() {
	string cakes;
	cin >> cakes;
	int k;
	cin >> k;
	
	int flips = 0;
	for (int i = 0; i+k <= cakes.size(); ++i) {
		if (cakes[i] == '-') {
			for (int j = i; j < i+k; ++j) {
				cakes[j] = cakes[j] == '-' ? '+' : '-';
			}
			flips++;
		}
	}
	
	for (int i = 0; i < cakes.size(); ++i) {
		if (cakes[i] != '+') {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << flips;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		test();
		cout << endl;
	}
	return 0;
}
