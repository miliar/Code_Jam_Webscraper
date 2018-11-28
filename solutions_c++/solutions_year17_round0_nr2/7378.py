#include<bits/stdc++.h>
using namespace std;

char s[100];

int main()
{
	int t;
	scanf("%d",&t);
	for(int it=1;it<=t;it++)
	{
		scanf("%s",s);
		for(int i=0;i<strlen(s)-1;i++)
		{
			if(s[i]-'0'<=s[i+1]-'0')
				continue;
			else
			{
				int j=i;
				if(j>=1&&s[j]-'1'>=s[j-1]-'0')
				{
					s[j]=s[j]-1;
				}
				else
				{
					while(j-1>=0&&s[j-1]==s[j])
						j--;
					s[j]=s[j]-1;
				}
				for(int k=j+1;k<strlen(s);k++)
					s[k]='9';
				if(s[0]=='0')
				{
					for(int k=0;k<strlen(s);k++)
					{
						s[k]=s[k+1];
					}
				}
				break;
			}
		}
		printf("Case #%d: %s\n",it,s);
	}
	return 0;
}