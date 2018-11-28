# include <bits/stdc++.h>
using namespace std;

int main()
{
	int T; cin >> T;
	for(int tt=1; tt<=T; ++tt) {
		string s; cin >> s;
		
		bool moar = true;
		while(moar) {
			moar = false;
			for(int i=0; i+1<s.size() && !moar; ++i) {
				if (s[i] > s[i+1]) {
					s[i] -= 1;
					for(int k=i+1; k<s.size(); ++k) {
						s[k] = '9';
					}
					moar = true;
				}
			}
		}
		
		printf("Case #%d: ", tt);
		
		bool lead = true;
		for(int i=0; i<s.size(); ++i) {
			if (s[i] == '0' && lead) continue;
			else {
				lead = false;
				printf("%c", s[i]);
			}
		}
		
		printf("\n");
	}
	return 0;
}