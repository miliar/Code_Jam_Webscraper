#include <stdio.h>
#include <string.h>

char s[1010];
int a[1010];
int main(void)
{
	int tt ,ii;
	int lens;
	int i;
	int ans;
	int tmp;
	int k;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%s %d" ,s+1 ,&k);
		lens=strlen(s+1);
		for (i=1 ; i<=lens ; i++)
		{
			a[i]=0;
		}
		ans=0;
		tmp=0;
		for (i=1 ; i+k-1<=lens ; i++)
		{
			if (a[i])
			{
				tmp^=1;
			}
			if ((s[i]=='-'&&tmp==0)||(s[i]=='+'&&tmp==1))
			{
				tmp^=1;
				ans++;
				a[i+k]=1;
			}
		}
		for (i=i ; i<=lens ; i++)
		{
			if (a[i])
			{
				tmp^=1;
			}
			if ((s[i]=='-'&&tmp==0)||(s[i]=='+'&&tmp==1))
			{
				ans=-1;
				break;
			}
		}
		printf("Case #%d: " ,ii);
		if (ans==-1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n" ,ans);
		}
	}
	
	return 0;	
}
