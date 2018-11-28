#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin>>T;
	for (int t=1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		string s;
		int k;
		cin>>s>>k;
		int n = s.size();
		int ans = 0;
		for (int i=0;i<=n-k;i++) {
			if (s[i] == '-') {
				ans++;
				for (int j=0;j<k;j++)
					s[i+j] = s[i+j] == '-' ? '+' : '-';
			}
		}
		bool ok = true;
		for (int i=0;i<n;i++)
			if (s[i] == '-')
				ok = false;
		
		if (!ok)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}