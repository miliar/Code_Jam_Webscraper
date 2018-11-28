#include <bits/stdc++.h>
using namespace std;


int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		string str;
		int k;
		cin >> str >> k;

		int cont = 0;

		for (int i = 0; i < str.size() - k +1; ++i) {
			if (str[i] == '-') {
				for (int j = 0; j < k; ++j)
					str[i+j] = (str[i+j] == '-' ? '+' : '-');

				cont += 1;
			}
		}

		for (int i = 0; i < k-1; ++i) {
			if (str[str.size() -i-1] == '-') {
				cont = -1;
			}
		}


		if (cont == -1) 
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t << ": " << cont << endl;

	}

	return 0;
}
