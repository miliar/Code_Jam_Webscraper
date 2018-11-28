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
		for(int q = 0; q < 20; q++)
		for(int j = 1; j < (int)s.size(); j++)
		{
			if(s[j] < s[j-1])
			{
				s = s.substr(0, j) + string(s.size() - j, '9');
				s[j-1]--;
				break;
			}
		}
		if(s[0] == '0')
			s.erase(s.begin() + 0);
		cout << "Case #" << i << ": " <<  s << "\n";
	}
}