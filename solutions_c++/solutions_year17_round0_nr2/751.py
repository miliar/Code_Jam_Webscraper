#include <bits/stdc++.h>

using namespace std;

char str[1010];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		int len;
		scanf("%s",str);
		len=strlen(str);
		int pos=len;

		for(int i=0;i<len-1;i++)
			if(str[i]>str[i+1])
			{
				pos=i;
				break;
			}
		if(pos<len)
		{
			for(int i=pos;i>=0;i--)
				if(i==0||str[i]>str[i-1])
				{
					pos=i;
					break;
				}
			str[pos]--;
			for(int i=pos+1;i<len;i++)
				str[i]='9';
		}

		printf("Case #%d: ",tt);

		int i=0;
		while(str[i]=='0')i++;
		for(;i<len;i++)
			printf("%c",str[i]);
		printf("\n");
	}

	return 0;
}