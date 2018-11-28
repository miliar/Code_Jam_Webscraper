#include <iostream>
#include <string>

using namespace std;

int solve(string s, int k) {
	int *arr = new int[s.length()]();
	int flip = 0;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == '-')
			++arr[i];
		if (i < s.length() - k + 1 && arr[i] % 2) {
			// Flip
			for (int j = 0; j < k; ++j)
				++arr[i + j];
			++flip;
		}
	}
	for (int i = 1; i < k; ++i) {
		if (arr[s.length() - k + i] % 2) {
			flip = -1;
			break;
		}
	}
	delete[](arr);
	return flip;
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		int k, res;
		cin >> s >> k;
		res = solve(s, k);
		cout << "Case #" << i + 1 << ": " 
		     << (res < 0 ? "IMPOSSIBLE" : to_string(res)) << endl;
	}
}