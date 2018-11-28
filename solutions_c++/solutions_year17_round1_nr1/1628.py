#include<stdio.h>
int main()
{
	int T,r,c,i,j,k,b,d;
	char a[27][27];
	FILE *fp2=fopen("result.txt","wt+");
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		scanf("%d %d",&r,&c);
		fprintf(fp2,"Case #%d:\n",i+1);
		for(j=0;j<r;j++)
		{
			scanf("%s",&a[j]);
		}
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				if(a[j][k]!='?')
				{
					for(b=j+1;b<r;b++)
					{
						if(a[b][k]=='?')
						{
							a[b][k]=a[j][k];
						}
						else
						break;
					}
				}
			}
		}
		for(k=0;k<c;k++)
		{
			for(j=0;j<r;j++)
			{
				if(a[j][k]=='?'&&j!=0)
				a[j][k]=a[j-1][k];
				else if(a[j][k]=='?')
				{
					for(b=j+1;b<r;b++)
					{
						if(a[b][k]!='?')
						{
							a[j][k]=a[b][k];
							break;
						}
					}
				}
			}
		}
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				if(a[j][k]=='?'&&k!=0)
				a[j][k]=a[j][k-1];
				else if(a[j][k]=='?')
				{
					for(b=k+1;b<c;b++)
					{
						if(a[j][b]!='?')
						{
							a[j][k]=a[j][b];
							break;
						}
					}
				}
			}
		}
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				fprintf(fp2,"%c",a[j][k]);
			}
			fprintf(fp2,"\n");
		}
	}
}
