#include <iostream>
#include <string>

using namespace std;

bool ok(const string &s) {
	for (int i=0; i<s.length()-1; ++i) {
		if (s[i] > s[i+1])
			return false;
	}
	return true;
}

string trim(const string &s) {
	int nz = s.find_first_not_of("0");
	if (nz == 0) {
		return s;
	}
	return s.substr(nz);
}

int main() {
	int T;
	long long N;
	cin >> T;
	for (int i=0; i<T; ++i) {
		string S;
		cin >> N;
		if (N) {
			while (N) {
				S += N % 10 + '0';
				N /= 10;
			}
			reverse(S.begin(), S.end());
		}
		else {
			S = "0";
		}
		//cout << "S=" << S << endl;
		if (S.length() == 1) {
			cout << "Case #" << (i+1) << ": " << S << endl;
		}
		else {
			while (!ok(S)) {
				for (int i=S.length()-1; i>0; --i) {
					if (S[i-1] > S[i]) {
						S[i-1]--;
						for (int j=i; j<S.length(); ++j) {
							S[j] = '9';
						}
					}
				}
			}
			cout << "Case #" << (i+1) << ": " << trim(S) << endl;
		}
	}
}