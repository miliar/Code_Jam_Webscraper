#include<bits/stdc++.h>
using namespace std;
int t,k;
string s;
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("jam.out");
	cin >> t;
	for(int i = 1; i<= t; i++)
	{
		int flip = 0;
		cin >> s >> k;
		for(int j = 0; j < s.length(); j++)
		{
			if(s[j] == '-' && s.length() - j >= k)
			{
				flip++;
				for (int q = j; q < j+k; q++)
				if (s[q] == '+')s[q] = '-';
				else s[q] = '+';
			}
		}
		bool u = false;
	//	cout << s << "\n";
		for(int j = 0; j < s.length(); j++)
		{
			if(s[j] == '-') u = true;
		}
		if(!u)cout << "Case #" << i <<": " << flip <<"\n";
		else cout << "Case #" << i <<": " << "IMPOSSIBLE" <<"\n";
	}
}
