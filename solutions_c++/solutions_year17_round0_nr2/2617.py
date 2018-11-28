#include <iostream>
#include <string>
using namespace std;

string s;
int len;
int ans[20];


void solve(){
	for (int i = 0; i < len; i++){
			int ok = 1;	
			long long x = 0;
			long long y = 0;
			for (int j = i; j < len; j++) {
				x = x*10+(s[i]-'0');
				y = y*10+(s[j]-'0');
			}
			if (x <= y)
				ok = 1;
			else ok = 0;

			if (ok)
				ans[i] = s[i]-'0';
			else {
				ans[i] = s[i]-'0'-1;
				for (int j = i+1; j < len; j++)
					ans[j] = 9;
				return;
			}
	}
}

int main() {
	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++){
		cin >> s;
		len = s.length();
		solve();
		cout << "Case #" << kase << ": ";
		int debut = 0;
		if (ans[0] == 0)
			debut = 1;
		for (int i = debut; i < len; i++)
			cout << ans[i];
		cout << endl;
	}
	return 0;
}