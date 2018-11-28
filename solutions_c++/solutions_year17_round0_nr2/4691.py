#include <bits/stdc++.h>

using namespace std;

int main() {
	size_t tc;
	cin >> tc;

	for (size_t t = 1; t <= tc; ++t) {
		string n;

		cin >> n;

		for (unsigned long long i = n.size()-1; i > 0; --i) {
			if (n[i-1] > n[i]) {
				n[i-1]--;
				for (size_t j = i; n[j] != '9' && j < n.size(); n[j++] = '9');
			}
		}

		unsigned long long i = 0;
		while (n[i] == '0') i++;

		cout << "Case #" << t << ": " << (n.c_str()+i) << '\n';
	}
}