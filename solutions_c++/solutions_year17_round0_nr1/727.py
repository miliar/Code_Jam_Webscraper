#include <bits/stdc++.h>

using namespace std;

typedef long long ll;




int main()
{
	ll casses;
	cin >> casses;
	for(int caseNum = 0; caseNum < casses; caseNum++)
	{
		string s;
		ll flips;
		cin >> s;
		cin >> flips;
		ll flipCount = 0;
		for(int i = 0; i <= s.size() - flips; i++)
		{
			if(s.at(i) == '-')
			{
				flipCount++;
				for(int j = 0; j < flips; j++)
				{
					if(s.at(i + j) == '-')
					{
						s.at(i + j) = '+';
					}else
					{
						s.at(i + j) = '-';
					}
				}
			}
			//cout << s << endl;
		}
		
		bool good = true;
		for(int i = 0; i < s.size(); i++)
		{
			if(s.at(i) == '-')
			{
				good = false;
				break;
			}
		}
		if(!good)
		{
			cout << "Case #" << caseNum+1 << ": IMPOSSIBLE" << endl;
		}else
		{
			cout << "Case #" << caseNum+1 << ": " << flipCount << endl;
		}
	
	}
	return 0;
}










