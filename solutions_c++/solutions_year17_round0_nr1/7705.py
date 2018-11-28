#include <bits/stdc++.h>
using namespace std ;
int main()
{
	int t;
	cin >>t;
	int p =1;
	while(t--)
	{
		cout << "Case #"<<p<<": ";
		char s[10000];
		cin >> s;
		int k;
		cin >> k;
		int i=0;
		int flag =0;
		int count=0;
		int ghh = strlen(s);
		while(s[i]!='\0')
		{
			if(s[i]=='-')
			{
				if(i+k-1>=ghh)
				{
					flag = 1;
					break;
				}
				count++;
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='-')
						s[i+j] = '+';
					else
						s[i+j] = '-';
				}

			}

			i++;
		}
		if(flag==1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << count <<endl;
		}

		p++;
	}
}
