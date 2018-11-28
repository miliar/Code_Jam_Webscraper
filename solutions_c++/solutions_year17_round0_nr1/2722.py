#include <iostream>
#include <cstdio>

using namespace std;

string s;
int k, t;

string flip(string s, int l, int r)
{
	string ans = s;
	for (int i = l; i < r; i++) {
		if (s[i] == '-')
			ans[i] = '+';
		else
			ans[i] = '-';
	}
	
	return ans;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		cin >> s >> k;
		int n = s.size();
		int ans = 0;
		
		for (int i = 0; i < n - k + 1; i++) {
			if (s[i] == '-') {
				s = flip(s, i, i + k);
				ans++;
			}
		}
		
		bool fl = 1;
		for (int i = 0; i < n; i++)
			if (s[i] == '-') {
				fl = 0;
				break;
			}
			
		cout << "Case #" << l + 1 << ": ";
		if (fl)
			cout << ans;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	
	
	return 0;
}
