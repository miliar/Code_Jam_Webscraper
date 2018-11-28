#include <bits/stdc++.h>
using namespace std;

string LLToStr(long long a) {
	ostringstream oss;
	oss << a;
	return oss.str();
}

long long StrToLL(string a) {
	long long res;
	istringstream iss(a);
	iss >> res;
	return res;
}

char IntToChar(int a) {
	return a + '0';
}

int CharToInt(char a) {
	return a - '0';
}

bool isOK(string a) {
	for (long long i=1; i<a.length(); i++) {
		if (a[i - 1] - '0' > a[i] - '0') {
			return false;
		}
	}
	return true;
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	long long t, n;

	cin >> t;

	for (long long i=1; i<=t; i++) {
		cin >> n;

		string ns = LLToStr(n);

		if (!isOK(ns)) {
			string tempStr = ns;
			if (ns.length() > 1) {
				if (ns[0] >= ns[1]) ns[0] = IntToChar(CharToInt(ns[0]) - 1);
			}
			ns[ns.length() - 1] = '9';
			for (long long j=ns.length() - 1; j>=1; j--) {
				bool isTrue = true;
				int temp = 9;
				if (ns[j] < ns[j - 1]) {
					ns[j] = '9';

					// int tempInt = CharToInt(ns[j - 1]) - 1;
					// if (tempInt < 0) tempInt = 9;
					// ns[j - 1] = IntToChar(tempInt);
				}
			}

			for (long long j=1; j<ns.length(); j++) {
				bool isTrue = true;
				int temp = 9;
				while(isTrue) {
					ns[j] = IntToChar(temp);
					if (StrToLL(tempStr) < StrToLL(ns) || ns[j] < ns[j - 1]) {
						temp--;
					} else {
						isTrue = false;
					}

					if (temp < 0) {
						isTrue = false;
					}
				}
			}
			// for (long long j=ns.length() - 2; j>=0; j--) {
			// 	bool isTrue = true;
			// 	int temp = 9;
			// 	while(isTrue) {
			// 		ns[j] = IntToChar(temp);
			// 		if (StrToLL(tempStr) < StrToLL(ns) || (CharToInt(ns[j]) > CharToInt(ns[j + 1]))) {
			// 			temp--;
			// 		} else {
			// 			isTrue = false;
			// 		}

			// 		if (temp < 0) {
			// 			isTrue = false;
			// 		}
			// 	}
			// }

			// if (ns[0] < tempStr[0]) {
			// 	for (long long j=1; j<ns.length() - 1; j++) {
			// 		bool isTrue = true;
			// 		int temp = 9;
			// 		while(isTrue) {
			// 			ns[j] = IntToChar(temp);

			// 			if (StrToLL(tempStr) < StrToLL(ns) || (CharToInt(ns[j]) < CharToInt(ns[j - 1]))) {
			// 				temp--;
			// 			} else {
			// 				isTrue = false;
			// 			}

			// 			if (temp < 0) {
			// 				isTrue = false;
			// 			}
			// 		}
			// 	}
			// }
		}

		cout << "Case #" << i << ": " << StrToLL(ns) << endl;
	}
}
