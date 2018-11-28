#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int n;
	string s;
	cin>>n;
	for(int z=1;z<=n;z++)
	{
	cin>>s;
	int k;
	cin>>k;
	int count1=0;
	for(int i=0;i+k<=s.length();i++)
	{
		if(s[i]=='-')
		{
			for(int j=i;j<i+k;j++)
			{
				if(s[j]=='-')
				s[j]='+';
				else if(s[j]=='+')
				s[j]='-';
			}
			count1++;
		}
	}
	bool flag=0;
	for(int i=0;i<s.length();i++)
	if(s[i]=='-')
	{
		flag=1;
		break;
	}
	if(flag)
	{
		printf("Case #%d: ",z);
		printf("IMPOSSIBLE\n");
	}
	else
	{
		printf("Case #%d: ",z);
		printf("%d\n",count1);
	}
}
	return 0;
}
