#include <iostream>
#include <string>
using namespace std;

void solve() {
	string N;
	cin >> N;
	int l = N.size();
	int p = 0;
	while (p+1 < l && N[p] <= N[p+1]) p++;
	if (p == l-1) {
		cout << N << endl;
		return;
	}
	for (int i = p+1; i < l; i++) {
		N[i] = '9';
	}
	while (p-1 >= 0 && N[p-1] > N[p]-1) N[p--] = '9';
	N[p]--;
	if (p == 0 && N[p] == '0') {
		cout << N.substr(1) << endl;
	} else {
		cout << N << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << (t+1) << ": ";
		solve();
	}
	return 0;
}
