#include <cstdio>
#include <iostream>
#include <cstring>

int main()
{
	int n;
	scanf("%d",&n);
	for (int i = 0; i < n; ++i)
	{	
		char s[1000]={};
		printf("Case #%d: " ,i+1);
		scanf("%s",s);
		int on = 0;
		int flag =1;
		if (strlen(s)==1)
		{
			printf("%s\n",s );
			continue;
		}
		while(s[on]==s[on+1])
			on++;
		if (on == strlen(s)-1)
		{
			printf("%s\n",s );
			continue;
		}
		else if (s [on+1] < s[on] && on != 0)
		{	
			if (s[0]!='1')
			{
				printf("%c",s[0]-1 );
			}
			for (int k = 0; k < strlen(s)-1; ++k)
			{
				printf("9");
			}
			printf("\n");
			continue;
		}
		for (int j = 0; j < strlen(s)-1; ++j)
		{
			if (s[j+1] < s[j] && s[j+1]!='0')
			{	
				printf("%c",s[j]-1 );
				for (int k = j; k < strlen(s)-1; ++k)
				{
					printf("9");
				}
				flag=1;
				printf("\n");
				break;
			}
			else if (s[j+1] < s[j] && s[j] == '1'&&s[j+1]=='0')
			{	
				for (int k = j; k < strlen(s)-1; ++k)
				{
					printf("9");
				}
				flag=1;
				printf("\n");
				break;
			}
			else if (s[j+1] < s[j] && s[j] != '1'&&s[j+1]=='0')
			{	
				printf("%c",s[j]-1 );
				for (int k = j; k < strlen(s)-1; ++k)
				{
					printf("9");
				}
				flag=1;
				printf("\n");
				break;
			}
			else{
				printf("%c",s[j]);
				flag=0;
			}
		}
		if (flag==0)
		{
			printf("%c\n",s[strlen(s)-1]);
		}
	}
	return 0;
}