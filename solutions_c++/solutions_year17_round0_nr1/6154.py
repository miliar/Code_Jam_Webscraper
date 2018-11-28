#include <bits/stdc++.h>

using namespace std;

int cnt = 1;
int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.txt","w",stdout);

	int test;
	cin >> test;

	while(test--)
	{
		string s;
		int k,check=0;
		cin >> s >> k;

		int ans = 0;

		for(int i=0;i<s.size();i++)
		{
			if(s.size()-i>=k && s[i] == '-')
			{
				for(int j=0,m=i;j<k;j++,m++)
				{
				  if(s[m] == '-')
					s[m] = '+';
				  else
					s[m] = '-';
				}
				ans++;
			}
		}
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='+')
				check++;
		}
		if(check == s.size())
			cout << "Case #"<<cnt<<": "<< ans << endl;
		else
			cout << "Case #"<<cnt<<": "<< "IMPOSSIBLE" << endl;

		cnt++;
	}
	return 0;
}
