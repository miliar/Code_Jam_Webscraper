#include <stdio.h>
#include <string.h>

char s[1010];
int main(void)
{
	int tt ,ii;
	int i ,j;
	int lens;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%s" ,s+1);
		lens=strlen(s+1);
		for (i=lens-1 ; i ; i--)
		{
			if (s[i]>s[i+1])
			{
				for (j=i+1 ; j<=lens ; j++)
				{
					s[j]='9';
				}
				s[i]--;
			}
		}
		if (s[1]=='0')
		{
			printf("Case #%d: %s\n" ,ii ,s+2);
		}
		else
		{
			printf("Case #%d: %s\n" ,ii ,s+1);
		}
	}
	
	return 0;	
}
