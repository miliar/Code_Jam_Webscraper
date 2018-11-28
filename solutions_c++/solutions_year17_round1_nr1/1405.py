#include <stdio.h>
char map[28][28],think[28][28];
int row[28];
void doe()
{
	int n,m,i,i2,l,r,i4,i3;
	scanf("%d %d",&n,&m);
	for(i=0;i<28;i++)
		row[i]=0;
	for(i=1;i<=n;i++)
		for(i2=1;i2<=m;i2++)
		{
			scanf(" %c",&map[i][i2]);
			if(map[i][i2]!='?')
			{
				row[i]=1;
			}	
		}
	row[n+1]=1;
	row[0]=1;
	for(i=1;i<=n;i++)
	{
		if(row[i]!=1)
			continue;
		i2=1;
		for(;map[i][i2]=='?';i2++);
		while(i2!=m+1)
		{
			for(i3=i2-1;map[i][i3]=='?';i3--);
			i3++;
			l=i3;
			for(i3=i2+1;map[i][i3]=='?';i3++);
			i3--;
			r=i3;
			//printf("%d %d\n",l,r);
			for(i3=l;i3<=r;i3++)
				map[i][i3]=map[i][i2];
			for(i3=i+1;row[i3]==0;i3++)
			{
				row[i3]==2;
				for(i4=l;i4<=r;i4++)
				{
					map[i3][i4]=map[i][i2];
				}
			}
			for(i3=i-1;row[i3]==0;i3--)
			{
				row[i3]==2;
				for(i4=l;i4<=r;i4++)
				{
					map[i3][i4]=map[i][i2];
				}
			}
			i2=r+1;
			for(;map[i][i2]=='?';i2++);
		}
	}
	printf("\n");
	for(i=1;i<=n;i++)
	{
		for(i2=1;i2<=m;i2++)
			printf("%c",map[i][i2]);
		printf("\n");
	}
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		doe();
	}
	return 0;
}