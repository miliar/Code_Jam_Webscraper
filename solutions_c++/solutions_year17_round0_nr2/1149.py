#include<stdio.h>
#include<string.h>
int main()
{
	freopen("output.txt", "w", stdout);
	int t, cas=0;
	scanf("%d", &t);
	while(t--)
	{
		char s[300]; scanf("%s", s);
		for(int i = strlen(s)-2; i >= 0; i--)
		{
			if(s[i] > s[i+1])
			{
				if(s[i] != '0') s[i]-=1;
				else 
				{
					s[i] = '9';
					s[i-1] -= 1;
				}
				for(int j = i+1; j < strlen(s); j++)
				s[j] = '9';
			}
		}
		if(s[0] == '0')
		{
			for(int i = 0; i < strlen(s)-1; i++)
			s[i] = s[i+1];
			s[strlen(s)-1] = '\0' ;
		}
		printf("Case #%d: %s\n", ++cas, s);
	}
}
