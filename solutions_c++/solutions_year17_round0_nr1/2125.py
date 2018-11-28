#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,tt,i,j,k,cnt;
	string str;
	cin >> t;
	for(tt=1;tt<=t;tt++)
	{
		cnt = 0;
		cin >> str >> k;
		for(i=0;i<str.length();i++)
		{
			if(str[i]=='-')
			{
				cnt++;
				if(i+k-1<str.length())
				{
					for(j=i;j<i+k;j++)
					{
						if(str[j]=='-')
							str[j] = '+';
						else
							str[j] = '-';
					}
				}
			}
		}
		//cout << str << endl;
		for(i=0;i<str.length();i++)
		{
			if(str[i]=='-')
				break;
		}
		cout << "Case #" << tt << ": "; 
		if(i==str.length())
			cout << cnt << endl;
		else
			cout << "IMPOSSIBLE" <<endl;
	}
	return 0;
}