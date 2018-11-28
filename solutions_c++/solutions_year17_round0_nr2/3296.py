#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);cout.tie(NULL);

	int T;cin >> T;
	string n;
	for(int t=1;t<=T;++t) {
		cin >> n;
		for(int i = n.size()-1; i > 0; --i)
			if(n[i] < n[i - 1]) {
				for(int j=i; j < n.size(); ++j) n[j] = '9';
				n[i - 1] = n[i - 1] - 1;
			}
		ll ans = atoll(n.c_str());
		cout << "Case #"<<t<<": "<<ans << endl;
	}
}
