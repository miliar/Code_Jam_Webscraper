#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;
		int l = 0, n = s.size();
		for (int i = 1; i < n; i++)
		{
			if (s[i] < s[i-1]) {
				s[l]--;
				for (int j = l+1; j < n; j++) s[j] = '9';
				if (s[l] == '0') s = s.substr(1);
				break;
			}
			if (s[i] > s[i-1]) l = i;
		}
		cout << "Case #" << t << ": " << s << endl;
	}
}
