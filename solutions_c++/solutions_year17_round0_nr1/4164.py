#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,k,st,f;
	cin >> t;
	for(int T=1;T<=t;T++)
	{
		char s[100000];cin >> s;cin >> k;
		st = 0 ; int len =strlen(s) ; f=0;
		for(int i=0; i < len ; i++)
		{
			if(s[i]=='-')
			{
				if( i+k-1 >= len)
					{f=1;break;}
				else
				{
					st++;
					for(int j=i;j<i+k && j<len;j++)
					{
						if(s[j]=='+')s[j]='-';
						else s[j]='+';
					}
				}
			}
		}
		if(f)
		cout << "Case #" << T << ": " << "IMPOSSIBLE" << endl;
		else
		cout << "Case #" << T << ": " << st << endl;
	}
}