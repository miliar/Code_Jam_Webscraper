#include <bits/stdc++.h>
using namespace std;


int main() {
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	bool ban;
	int t, n, size, changes, c = 0;
	cin >> t; 
	string s;
	while(c<t) {
		c++;
		ban = true;
		cin >> s >> n;
		size = s.size();
		changes = 0;
		for(int i = 0; i <= (size-n); i++){
			if(s[i] == '-') {
				changes++;
				for(int j = 0; j < n; j++) {
					s[i+j] = (s[i+j])=='-'?'+':'-';
				}
			}
		}
		cout << "Case #" << c << ": ";
		for(int i = 0; i < size; i++) {
			if(s[i] == '-') {
				ban = false;
				cout << "IMPOSSIBLE\n";
				break;
			}
		}
		if(ban) {
			cout << changes <<"\n";
		}
	}
	return (0);
}