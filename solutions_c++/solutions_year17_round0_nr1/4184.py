#include <bits/stdc++.h>
using namespace std;

int main()
{
	int tst;
	scanf("%d",&tst);
	for(int t=1;t<=tst;t++)
	{
		getchar();
		string s;
		int n;
		cin>>s;
		scanf("%d",&n);
		int len = s.length(),cnt=0;
		for(int i=0;i<len;i++)
		{
			if(s[i] == '-')
			{
				if(i > len-n) 
				{
					cnt=-1;
					break;
				}
				cnt++;
				for(int j=i;j<i+n;j++)
				{
					if(s[j]=='-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		if(cnt==-1) 
			printf("Case #%d: IMPOSSIBLE\n",t);
		else
			printf("Case #%d: %d\n",t,cnt);
	}
}
