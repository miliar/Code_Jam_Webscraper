#include<bits/stdc++.h>
using namespace std;
bool ok(int i) {
	int last = 9;
	while (i > 0) {
		int r = i % 10;
		if (r > last) return false;
		last = r;
		i /= 10;
	}
	return true;
}
int main() {
	int T; cin >> T;
	for (int tc=1; tc<=T; tc++) {
		int N; cin >> N;
		int ans = 0;
		for (int i=1; i<=N; i++) if (ok(i)) ans = i;
		cout << "Case #"<<tc<<": "<<ans << endl;
	}
}
