#include <bits/stdc++.h>

using namespace std;

int main() {
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	string s;
	int cnt,k;
	
	int n;
	cin >> n;
	for(int zzzz=0;zzzz<n;zzzz++) {
		cin >> s;
		int flg = 0;
		while(true) {
			flg = 0;
			for(int i=1;i<s.length();i++) {
				if(s[i] < s[i-1]) {
					for(int j=i;j>=0;j--) {
						if(s[j] > '0') {
							s[j]--;
							for(int k=j+1;k<s.length();k++) {
								s[k] = '9';
							}
							break;
						}
					}
					flg = 1;
				}
			}
			if(!flg)
				break;
		}
		flg = 0;
		cout << "Case #" << zzzz+1 << ": ";
		for(int i=0;i<s.length();i++) {
			if(s[i] != '0') {
				flg = 1;
			}
			if(flg)
				cout << s[i];
		}
		cout << '\n';
	}
	
	return 0;
}
