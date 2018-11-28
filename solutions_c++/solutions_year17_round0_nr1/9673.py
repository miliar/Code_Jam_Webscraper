#include <bits/stdc++.h>

using namespace std;

#define SZ(x) (int)(x).size()
#define ALL(X) (X).begin(),(X).end()
#define ALLR(X) (X).rbegin(),(X).rend()
typedef vector<int> vi;

string toString(int a) {
	ostringstream temp;
	temp << a;
	return temp.str();
}

char flip(char x) {
	if (x == '-') {
		x = '+';
	} else {
		x = '-';
	}
	return x;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int h = 0, s = 1, n, t, k, p;
	string m, z;
	cin >> t;

	while (t--) {
		h = 0;
		cin >> m >> k;
		for (int i = 0; i <= SZ(m) - k; ++i) {
			if (m[i] == '-') {
				h++;
				for (int j = 0; j < k; ++j) {
					m[i + j] = flip(m[i + j]);
				}
			}
			//		cout << m << " " << h << endl;

		}
		z = m;
		for (int i = 0; i < SZ(m); ++i) {
			z[i] = '+';
		}
		if (m == z) {
			cout << "case #" << s << ": " << h << endl;
		} else {
			cout << "case #" << s << ": " << "IMPOSSIBLE" << endl;
		}
		s++;
	}
	return 0;
}
