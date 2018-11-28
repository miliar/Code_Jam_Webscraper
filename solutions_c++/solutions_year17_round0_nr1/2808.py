#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <=t; i++)
	{
		string s;
		cin >> s;
		int n;
		cin >> n;
		int ans = 0;
		for(int i = 0; i + n  - 1 < s.size(); i++)
		{
			if(s[i] == '-')
			{
				ans  ++;
				for(int j  = 0; j < n; j++)
					s[i + j] = s[i+j] == '-' ? '+' : '-';
			}	
			
		}
		if(s != string(s.size(), '+'))
			cout << "Case #" << i << ": " <<  "IMPOSSIBLE" << "\n";
		else		
			cout << "Case #" << i << ": " <<  ans << "\n";
	}
}