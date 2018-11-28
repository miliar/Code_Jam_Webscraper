#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define ff first
#define ss second
#define mp make_pair
#define pb push_back

typedef long long llong;
typedef pair<int, int> pii;

void process() {

	string str;
	cin >> str;

	int n = str.size();
	char prev_digit = str[0];

	for (int i = 1; i < n;) {

		char c = str[i];

		// violation
		if (c < prev_digit) {

			str[i - 1] = (char)(str[i - 1] - 1);

			for (int j = i; j < n; j++) {
				str[j] = '9';
			}
			
			i -= 2;

			if (i < 0) {
				i++;
			}

			prev_digit = str[i];

			// cout << "prev digit " << prev_digit << endl;

		} else {
			prev_digit = c;
			i++;
		}

	}

	if (str[0] == '0') {
		cout << str.substr(1);
	} else {
		cout << str;
	}

}

void solve() {

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {

		cout << "Case #" << (i + 1) << ": ";
		process();
		cout << endl;

	}
	

}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	#ifdef LOCAL
		ifstream in("in");
		cin.rdbuf(in.rdbuf());

		ofstream out("out");
		cout.rdbuf(out.rdbuf());
	#endif

	solve();

	return 0;

}