#include <iostream>
#include <stdio.h>

using namespace std;

int t, k;
string s;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	int now = 0;
	
	while(t--) {
		cin >> s >> k, now++;
		
		int a = 0, ans = 0;
		cout << "Case #" << now << ": ";
		
		for(int i=0; i <= s.length()-k; i++)
			if(s[i] == '-') {
				for(int h=i; h < i+k; h++) {
					if(s[h] == '-')
						s[h] = '+';
					else
						s[h] = '-';
				}
				ans++;
			}
		
		for(int i=0; i < s.length(); i++)
			if(s[i] == '-') {
				cout << "IMPOSSIBLE\n";
				a = 1;
				break;
			}
		if(a == 1)
			continue;
		
		cout << ans << "\n";
	}
}
