#include <iostream>
#include <string>

using namespace std;
typedef long long ll;

int main() {
	ll t;
	cin >> t;
	for (ll k = 1; k <= t; k++) {
		string s;
		cin >> s;	
		ll l = s.length(), i;	
		for (i = 0; i <= l - 2; i++) {
			if (s[i] > s[i + 1]) {
				break;
			}
		}
		if (i == l - 1) {
			cout << "Case #" << k << ": " << s << "\n";
		} else {
			ll j;
			for (j = i; j > 0; j--) {
				if (s[j - 1] < s[j]) {
					break;
				}
			}
			i = j;
			cout << "Case #" << k << ": ";
			for (j = 0; j < l; j++) {
				if (j < i) {
					cout << s[j];
				} else if (j == i) {
					char temp = static_cast<char>(s[i] - 1);
					if (!(temp == '0' && j == 0)) {
						cout << temp;
					}
				} else {
					cout << "9";
				}
			}
			cout << "\n";
		}
	}
	return 0;
}