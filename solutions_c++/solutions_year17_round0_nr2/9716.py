#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;
int a[20], x, n, t;
string str;
int main()
{	
	cin >> t;
	for (int j = 1; j <= t; j++)
	{
		cin >> str;
		bool u = 0, s = 1, m = 1; n = 0;
		cout << "Case #" << j << ": ";
		for (char c : str)
		{
			a[++n] = (c-'0'), u |= (c > '1' && c <= '9');
			if (c == '0') m = u;
		}
		for (int i = 1; i < n; i++) s &= (a[i] <= a[i+1]);
		if (!s)
			if (!m) {for (int i=1; i < n; i++) a[i] = 9; a[n] = -1;}
			else{
				for (int i = 1; i <= n; i++)
					if (a[i] >= a[i+1]){a[i++]--; while(i<=n)a[i++] = 9;}
			}
		for (int i = 1; i <= n; i++) if (a[i] != -1) cout << a[i];
		cout << "\n";
	}
}
