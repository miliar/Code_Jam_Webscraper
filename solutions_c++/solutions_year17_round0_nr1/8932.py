#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("C:\\Users\\Abhishek\\Desktop\\Google Code Jam\\2017 Qualification Round\\A-large.in", "r", stdin);
	freopen("C:\\Users\\Abhishek\\Desktop\\Google Code Jam\\2017 Qualification Round\\A-output_large.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		string s;
		int k, f = 0;
		cin >> s >> k;
		int n = s.length();
		int ans = 0;
		for(int i = 0; i <= n - k; i++)
		{
			if(s[i] == '-')
			{
				ans++;
				for(int j = i; j < i + k; j++)
				{
					if(s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
			else
				continue;
		}
		
		for(int i = n - k; i < n; i++)
		{
			if(s[i] == '-')
			{
				f = 1;
				break;
			}
		}
		
		if(f == 1)
			cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << test << ": " << ans << endl;	
	}
}

