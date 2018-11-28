#include <bits/stdc++.h>
#define endl '\n'
#define Int long long
#define pb push_back
#define mp make_pair
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int cnt_tests;
	cin>>cnt_tests;

	for(int cs = 1; cs <= cnt_tests; cs++) {
		string s;
		int k;
		
		cin>>s>>k;
	
		int ans = 0;
		for(int i = 0; i < s.size() - k + 1; i++) {
			if(s[i] == '-') {
				for(int j = 0; j < k; j++) {
					if(s[i + j] == '-') {
						s[i + j] = '+';
					}
					else {
						s[i + j] = '-';
					}
				}

				ans++;
			}
		}

		for(int i = 0; i < s.size(); i++) {
			if(s[i] == '-') {
				ans = -1;
				break;
			}
		}

		cout<<"Case #"<<cs<<": ";
		if(ans == -1) {
			cout<<"Impossible"<<endl;
		}
		else {
			cout<<ans<<endl;
		}
	}

	return 0;
}
