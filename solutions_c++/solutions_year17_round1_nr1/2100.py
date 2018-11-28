#include<stdio.h>
#include<ctype.h>
int main()
{
	int t, r, c, i, j, k, j2, k2, hml, b;
	char table[25][25], cc;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d", &r, &c);
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				table[j][k]=0;
				while(!isalpha(table[j][k])&&table[j][k]!='?')
					scanf("%c",&(table[j][k]));
			}
		}

		hml=0;
		b=0;
		for(j=0;j<r;j++)
		{
			cc='?';
			b=0;
			for(k=0;k<c;k++)
			{
				if(table[j][k]!='?')
				{
					if(cc=='?')
						cc=table[j][k];
					else
					{
						for(j2=j-hml;j2<=j;j2++)
						{
							for(k2=b;k2<k;k2++)
								table[j2][k2]=cc;
						}
						b=k;
						cc=table[j][k];
					}
				}
				
			}
			if(cc=='?')
				hml++;
			else
			{
				for(j2=j-hml;j2<=j;j2++)
				{
					for(k2=b;k2<k;k2++)
						table[j2][k2]=cc;
				}
				hml=0;
			}
		}
		if(hml>0)
		{
			for(j=r-hml;j<r;j++)
			{
				for(k=0;k<c;k++)
					table[j][k]=table[r-hml-1][k];
			}
		}

		printf("Case #%d:\n",i+1);
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
				printf("%c",table[j][k]);
			printf("\n");
		}
	}
	return 0;
}
