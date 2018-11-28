#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		string n;
		cin >> n;
		string res = n;
		bool done = false;
		while (!done) {
			done = true;
			for (auto i = 0; i + 1 < res.size(); ++i) {
				if (res[i] > res[i+1]){
					done = false;
					res[i] -= 1;
					for (int j = i + 1; j < res.size(); ++j) res[j] = '9';
					break;
				}
			}
		}

		if (res[0] == '0') res = res.substr(1);

		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}
