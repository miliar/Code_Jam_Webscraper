#include <bits/stdc++.h>
#define endl '\n'
#define Int long long
#define pb push_back
#define mp make_pair
using namespace std;

bool is_tidy(int num) {
	vector<int> digs;
	
	while(num > 0) {
		digs.pb(num % 10);
		num /= 10;
	}

	for(int i = digs.size() - 1; i >= 1; i--) {
		if(digs[i] > digs[i - 1]) {
			return false;
		}
	}

	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int cnt_tests;
	cin>>cnt_tests;

	for(int cs = 1; cs <= cnt_tests; cs++) {
		int n;
		cin>>n;

		int ans;
		for(int i = n; i >= 1; i--) {
			if(is_tidy(i)) {
				ans = i;
				break;
			}
		}

		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}

	return 0;
} 
