#include <iostream>
#include <string>
#include <utility>
using namespace std;

typedef long long lint;
typedef pair<lint, lint> intp;

intp go(lint n, lint k) {
	if (k > n) {
		cout << "ERROR: " << k << " > " << n << endl;
	}
	if (k == 1)
		return intp(n / 2, (n - 1) / 2);
	else if (k % 2 == 0) {	// even
		return go(n / 2, k / 2);
	}
	else {
		return go((n - 1) / 2, k / 2);
	}
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output3L.txt","w", stdout);
    
	int T; cin >> T;
	lint n, k;
	for (int c = 1; c <= T; ++c) {
		cin >> n >> k;
		intp res = go(n, k);
		cout << "Case #" << c << ": "
			<< res.first << ' '
			<< res.second << endl;
	}
}