#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin>>T;
	for (int t=1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		string s;
		cin>>s;
		int n = s.size();
		char ans[100];
		for (int i=0;i<n;i++) {
			bool canBeTheSame = true;
			for (int j=i+1;j<n;j++) {
				if (s[j] < s[i]) {
					canBeTheSame = false;
					break;
				}
				if (s[j] > s[i]) {
					canBeTheSame = true;
					break;
				}
			}
			if (canBeTheSame) {
				ans[i] = s[i];
			}
			else {
				ans[i] = s[i]-1;
				for (int j=i+1;j<n;j++) {
					ans[j] = '9';
				}
				break;
			}
		}
		for (int i=0;i<n;i++)
			if (ans[i] != '0') {
				for (int j=i; j < n; j++)
					cout << ans[j];
				cout << endl;
				break;
			}
	}
	return 0;
}