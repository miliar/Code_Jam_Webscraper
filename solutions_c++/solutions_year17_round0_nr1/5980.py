#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

typedef signed long long longf;
typedef unsigned long long ulongf;

int t;
string str;
int k, len;

int search_la () {
	len = str.length();
	// cout << str;

	for (int i = 0; i < len; ++i) {
		if (str.find("-", 0) == string::npos) {
			// cout << endl;
			return i;
		}

		for (int j = 0; j <= len - k; ++j) {
			if (str[j] == '-') {
				auto f = str.substr(j, k);

				for (int i = 0; i < f.length(); ++i)
					if (f[i] == '+') f[i] = '-';
					else f[i] = '+'; 

				str.erase(j, k);
				str.insert(j, f);

				// cout << " -> " << str;

				break;
			}
		}
	}

	// cout << endl;
	return -1;
}

int main() {
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		cin >> str >> k;
		int ans = search_la();
		if (ans < 0) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}

	return 1;
}