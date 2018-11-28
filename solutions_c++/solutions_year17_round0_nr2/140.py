#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

void solve() {
	string s;
	cin >> s;
	int n = int(s.length());
	for (int i = 1; i < n; ++i) if (s[i - 1] > s[i]) {
		int f;
		for (f = i; f > 0 && s[f - 1] == s[i - 1]; --f);
		for (int j = 0; j < f; ++j)
			cout << s[j];
		if (f != 0 || s[f] != '1')
			cout << char(s[f] - 1);
		for (int j = f + 1; j < n; ++j)
			cout << '9';
		cout << '\n';
		return;
	}
	cout << s << '\n';
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}
