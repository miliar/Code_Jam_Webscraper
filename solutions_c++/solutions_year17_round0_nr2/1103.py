#include <bits/stdc++.h>

using namespace std;

int t,l,pnt;
char number[30],ans[30];

int main()
{
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%s",number);
		l=strlen(number);
		ans[0]=number[0];
		for(int i=1;i<l;i++)
		{
			if(ans[i-1] <= number[i])
				ans[i]=number[i];
			else
			{
				ans[i-1] = ans[i-1]-1;
				for(int j=i;j<l;j++)
					ans[j]='9';
				pnt=i-1;
				while(ans[pnt]<ans[pnt-1])
				{
					ans[pnt-1]=ans[pnt-1]-1;
					for(int j=pnt;j<l;j++)
						ans[j]='9';
					pnt--;
				}
				break;
			}
		}
		pnt =0;
		while(ans[pnt] =='0')
			pnt++;
		printf("Case #%d: ",k);
		while(pnt<l)
		{
			printf("%c",ans[pnt]);
			pnt++;
		}
		printf("\n");
	}
	
	return 0;
}
