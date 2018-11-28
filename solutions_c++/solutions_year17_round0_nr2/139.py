#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		string str;
		cin >> str;

		for(int i=str.size()-2; i>=0; i--)
		{
			if(str[i]>str[i+1])
			{
				str[i]--;
				for(int j=i+1; j<str.size(); j++)
					str[j] = '9';
			}
		}

		int startpos = 0;
		if(str[0]=='0')
			startpos = 1;

		cout << "Case #" << cn << ": " << str.substr(startpos) << endl;
	}
}