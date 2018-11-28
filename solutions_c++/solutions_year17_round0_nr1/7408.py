#include <iostream>

using namespace std;

int count;
int T, k;
string s;

bool verify(int size) {

	for (int i = 0; i < size; ++i) {

		if ((s[i] == '-') && (size - i) >= k) {
			count++;
			for (int j = 0; j < k; ++j) {
				(s[i + j] == '-') ? s[i + j] = '+' : s[i + j] = '-';
			}
		}
	}

	for (int i = 0; i < size; ++i) {
		if (s[i] == '-') {
			return false;
		}
	}

	return true;
}

int main(int argc, char const *argv[]) {


	int c = 0;
	cin >> T;

	while (T--) {

		count = 0;

		cin >> s >> k;

		int size = s.size();

		cout << "Case #" << ++c << ": ";

		if(verify(size)) {
			cout << count << "\n";	
		}
		else
			cout << "IMPOSSIBLE\n";

	}

	return 0;
}