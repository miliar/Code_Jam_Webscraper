#include <iostream>
#include <string>
using namespace std;

bool test(int n)
{
	string s = std::to_string(n);
	for (int i = 0; i < s.size() - 1; i++) {
		if (s[i] > s[i + 1]) {
			return false;
		}
	}
	return true;
}

int main() {
	int T, N;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		cin >> N;
		do {
			if (test(N)) {
				cout << "Case #" << kase << ": " << N << endl;
				break;
			}
		} while (--N);
	}
}