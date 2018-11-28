#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	freopen("input22.txt", "r", stdin);
  	freopen("output24.txt", "w", stdout);

	cin >> t;
	for(int i=1;i<=t;i++)
	{
		char s[1005];
		scanf("%s",s);
		int k;
		cin >> k;
		cout << "Case #" << i << ": ";
		int c=0;
		for(int j=0;j<strlen(s);j++)
		{
			if(s[j]=='-')
			{
				if(j+k<=strlen(s))
				{
					c++;
					for(int m=j;m<j+k;m++)
					{
						if(s[m]=='+') s[m]='-';
						else s[m]='+';
					}
				}
			}
		}
		int f=0;
		for(int j=0;j<strlen(s);j++)
		{
			if(s[j]=='-')
				f=1;
		}
		if(f!=1)
		cout << c << endl;
		else cout << "IMPOSSIBLE\n";
	}
}
