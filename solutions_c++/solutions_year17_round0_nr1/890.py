#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; ++tc)
	{
		string s;
		int k;
		cin >> s >> k;
		int res = 0;
		bool flag = true;
		for(int i=0;i<s.size();++i)
		{
			if(s[i]=='-')
			{
				if(i+k-1<s.size())
				{
					++res;
					for(int j=0;j<k;++j)
						if(s[i+j]=='+')
							s[i+j] = '-';
						else
							s[i+j] = '+';
				}
				else
				{
					flag = false;
					break;
				}
			}
		}
		if(flag)
			cout << "Case #" << tc << ": " << res << endl;
		else
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
