#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string s;
int t,n,k;

int main() 
{
	freopen("f.txt","r",stdin);
	freopen("fout.txt","w",stdout);
	cin >> t;
	int c = 1;
	while(t--) {
		cin >> s >> k;
		int ans = 0;
		cout << "Case #" << c++ << ": ";
		for(int i = 0; i < s.size(); i++) {
			if(s[i] == '-') {
				ans ++;
				if(i + k <= s.size())
				for(int j = i; j < i + k; j++) {
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		bool ok = 1;
		for(int i = 0; i < s.size(); i++) {
			if(s[i] == '-') {
				ok = 0;
				puts("IMPOSSIBLE");
				break;
			}
		}
		if(ok == 1) {
			cout << ans << '\n';
		}
	}

	return 0;
}