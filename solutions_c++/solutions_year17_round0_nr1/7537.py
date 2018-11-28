#include <bits/stdc++.h>
using namespace std;

int T, K, ans;
string s;
bool rev[1002], side, err;


int main() {
	cin>>T;
	for (int i=0; i<T; i++) {
		cin >> s >> K;
		side = 0, ans = 0;
		for (int i=0; i<1002; ++i) rev[i] = 0;
		unsigned j=0;
		for(; j<=s.length()-K; ++j) {
			side ^= rev[j];
			if ( (s[j] == '-') ^ side){
				side^= 1;
				++ans;
				rev[j+K]^=1;
			}
		}
		err = 0;
		for ( ; !err && j<s.length(); ++j) {
			side ^=rev[j];
			if (side ^ (s[j] == '-')) err = 1;
		}
		cout<<"Case #"<<i+1<<": ";
		if (err) cout << "IMPOSSIBLE" << "\n";
		else cout << ans << "\n";
	}
	return 0;
}
