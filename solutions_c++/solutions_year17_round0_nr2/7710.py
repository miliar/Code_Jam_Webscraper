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
		char s[100] ;
		cin >> s;
		int i = 0;
		int ghh =-1;
		int last = 0;
		while(s[i]!='\0')
		{

			int df = (int) s[i] - (int)'0';
			if(df<last)
			{
				ghh = last;
				break;
			}
			last = df ;
			i++;
		}
		if(ghh==-1)
		{
			cout << s<<endl;
			p++;
			continue;
		}
		int dfd = strlen(s);
		int sa = -1;
		for(i=0;i<dfd;i++)
		{
			int df = (int) s[i] - (int)'0';
			if(sa==1)
			{
				cout << "9";
			}
			else
			{
				if(df<ghh)
				{
					cout << s[i];
				}
				if(df==ghh)
				{
					if(df==1)
					{
						sa  = 1;
						continue;
					}
					cout << df - 1;
					sa  = 1;
				}

			}

		}
		cout << endl;
		


		p++;
	}
}
