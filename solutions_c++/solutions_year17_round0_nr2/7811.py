#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int c = 1; c <= t; ++c) {
		cout << "Case #" << c << ": ";
		string k;
		cin >> k;
		int idx_9 = k.size();
		
		for (int i = k.size() - 1; i > 0; --i) {
			int a, b;
			a = k[i-1] - '0';
			b = k[i] - '0';
			if (a>b) {
				idx_9 = i;
				k[i-1] = k[i-1]-1;
			}
		}
		
		if (k[0] != '0')
			cout << k[0];
		for (int i = 1; i < idx_9; ++i)
		{
			cout << k[i];
		}
		for (int i = idx_9; i < k.size(); ++i) {
			cout << "9";
		}

		cout << endl;
		// return 0;
	}
	return 0;
}