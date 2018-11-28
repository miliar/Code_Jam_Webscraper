#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;

	cin >> t;
	for (int caso = 1; caso <= t; ++caso) {
		string cad;
		int t;

		cin >> cad >> t;
		vector<int> data(cad.size());
		for (int i = 0; i < cad.size(); ++i)
			data[i] = (cad[i] == '+');

		int ans = 0;
		for (int i = 0; i < data.size(); ++i) {
			while (i < data.size() && data[i]) ++i;
			if (i + t  - 1 >= cad.size()) break;

			ans++;
			for (int j = 0; j < t; ++j)
				data[i + j] = 1 - data[i + j];
		}
		
		bool valid = true;
		for (const auto &var : data)
			if (!var) {
				valid = false;
				break;
			}

		cout << "Case #" << caso << ": ";
		if (valid)
			cout << ans << '\n';
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}

