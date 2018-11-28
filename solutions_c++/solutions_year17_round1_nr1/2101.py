#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	for (int t = 1; t <= nTests; ++t) {
		int r, c;
		cin >> r >> c;
		vector<string> cake(r);
		for (int i = 0; i < r; ++i)
			cin >> cake[i];
		cout << "Case #" << t << ":" << endl;

		for (int i = 0; i < r; ++i) {
			char first = '?', last = '?';
			for (int j = 0; j < c; ++j) {
				if (cake[i][j] == '?') {
					if (last != '?')
						cake[i][j] = last;
					continue;
				}
				if (first == '?')
					first = cake[i][j];
				last = cake[i][j];
			}
			if (first != '?') {
				for (int j = 0; j < c; ++j) {
					if (cake[i][j] != '?')
						break;
					cake[i][j] = first;
				}
			}
		}
		vector<int> ref(r, -1);
		int first = -1, last = -1;
		for (int i = 0; i < r; ++i) {
			if (cake[i].front() == '?') {
				if (last >= 0)
					ref[i] = last;
				continue;
			}
			if (first < 0)
				first = i;
			last = i;
			ref[i] = i;
		}
		for (int i = 0; i < r; ++i) {
			if (ref[i] < 0)
				cout << cake[ref[first]] << endl;
			else
				cout << cake[ref[i]] << endl;
		}
	}
	return 0;
}
