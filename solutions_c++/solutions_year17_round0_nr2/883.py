#include<bits/stdc++.h>
using namespace std;

string stringRepeat(char c, int n)
{
	string s;
	while(n--)
		s += c;
	return s;
}

string f(string s, int idx, char c)
{
	for(int i=idx;i<s.size();++i)
		s[i] = c;
	return s;
}

int main()
{
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; ++tc)
	{
		string s, res;
		cin >> s;
		
		if(s.size() == 1)
			res = s;
		else
		{
			res = stringRepeat('9', s.size()-1);
			string tmp = stringRepeat('1', s.size());
			if(tmp <= s)
			{
				res = tmp;
				for(int i=0;i<res.size();++i)
					for(char c=res[i]; c <= '9'; ++c)
						if(f(res, i, c) <= s)
							res = f(res, i, c);
			}
		}

		cout << "Case #" << tc << ": " << res << endl;
	}
	return 0;
}
