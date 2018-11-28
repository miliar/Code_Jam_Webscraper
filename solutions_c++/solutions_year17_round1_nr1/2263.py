#include <iostream>
#include <vector>


using namespace std;


int main() {
	int T, t;
	cin >> t; T = t;
	while (t--) {
		int R, C;
		cin >> R >> C;
		vector< vector<char> > cake(R); 
		vector<int> nemp(R, 0); vector<char> lat;
		int i, j, k; char c, latest;
		for (i = 0; i< R; ++i) {
			for (j = 0; j < C; ++j) {
				cin >> c;
				cake[i].push_back(c);
				if (c != '?')
					nemp[i] = 1;
			}
		}

		for (i = 0; i< R; ++i) {
			if (!nemp[i])
				continue;
			j = 0;
			while (cake[i][j] == '?')
				j++;
			latest = cake[i][j];
			for (k = 0; k < j; ++k)
				cake[i][k] = latest;
			for (k = j + 1; k < C; ++k) {
				if (cake[i][k] == '?')
					cake[i][k] = latest;
				else
					latest = cake[i][k];
			}
		}

		i = 0;
		while(!nemp[i])
			i++;
		lat = cake[i];

		for (k = 0; k < i; ++k)
			cake[k] = lat;

		for (k = i + 1; k < R; ++k) {
			if (!nemp[k])
				cake[k] = lat;
			else 
				lat = cake[k];
		}

		cout << "Case #" << T - t << ":\n";
		for (i = 0; i < R; ++i) {
			for (j = 0; j < C; ++j)
				cout << cake[i][j];
			cout << "\n";
		}




	}

	return 0;
}