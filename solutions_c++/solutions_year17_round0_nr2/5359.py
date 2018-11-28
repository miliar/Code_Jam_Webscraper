#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

vector<int> fix(vector<int> v) {
	int q = v.size();
	for (;;) {
		int wrong = -1;
		for (int i = 0; i < q - 1; ++i) {
			if (v[i] > v[i + 1]) {
				wrong = i;
				break;
			}
		}
		if (wrong == -1) return v;
		--v[wrong];
		for (int i = wrong + 1; i < q; ++i) {
			v[i] = 9;
		}
	};
}

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		string s, r;
		cin >> s;
		int q = s.size();
		vector<int> v(q);
		for (int i = 0; i < q; ++i) {
			v[i] = s[i] - '0';
		}
		bool front = true;
		for (auto d : fix(v)) {
			if (!(front && d == 0)) {
				front = false;
				r += d + '0';
			}
		}
		cout << "Case #" << test << ": " << r << endl;
	}
}