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
		cnt = 0;
		cin >> s >> k;
		for(int i=0;i<s.length()-k+1;i++) {
			if(s[i] == '-') {
				cnt++;
				for(int j=i;j<i+k;j++) {
					if(s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}
		int flg = 0;
		for(int i=0;i<s.length();i++) {
			if(s[i] == '-') {
				flg = 1;
				break;
			}
		}
		if(flg)
			cout << "Case #" << zzzz+1 << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << zzzz+1 << ": "  << cnt << '\n';
			
	}
	
	return 0;
}
