#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		string s;
		int a[30];
		memset(a, 0, sizeof a);
		cin >> s;
		int n = s.length();
		for(int i = 0; i < n; i++)
			a[i] = s[i] - '0';
		bool ok = false;
		while(!ok)
		{
			ok = true;
			for(int i = 0; i < n - 1; i++)
				if(a[i] > a[i+1])
				{
					ok = false;
					a[i]--;
					for(int j = i + 1; j < n; j++)
						a[j] = 9;
				}
		}
		cout << "Case #" << t << ": ";
		if(a[0] == 0 && n > 1) 
			for(int i = 1; i < n; i++) cout << a[i];
		else
			for(int i = 0; i < n; i++) cout << a[i];
		cout << "\n";
	}
	return 0;
}