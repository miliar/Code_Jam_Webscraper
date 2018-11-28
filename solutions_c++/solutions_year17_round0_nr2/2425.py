#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

char num[34];

int main()
{
	int T;
	cin >> T;
	for(int tc=1;tc<=T;tc++)
	{
		scanf("%s", num);
		int len = strlen(num);
		
		for(int i=len-1;i>0;i--)
		{
			if(num[i]<num[i-1])
			{
				for(int j=i;j<len;j++)
				{
					num[j] = '9';
				}
				num[i]='9';
				num[i-1]--;
			}
		}
		printf("Case #%d: ",tc);
		if(num[0]=='0') printf("%s\n", num+1);
		else printf("%s\n", num);
	}

	return 0;
}
