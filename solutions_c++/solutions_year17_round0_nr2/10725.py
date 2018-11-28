#include<stdio.h>
void check(int a[],int l,int test)
{
	int i,j;
	int count=0;
	for (i=0;i<l-1;i++)
	{
		if (a[i]>=a[i+1])
		{
			count=count+1;
		}
	}
	if (count==l-1)
	{
		printf("Case #%d: ",test);
		for (i=l-1;i>=0;i--)
		{
			printf("%d",a[i]);
		}
		printf("\n");
		return;
	}
	else
	{
		if (a[0]!=0)
		{
			a[0]=a[0]-1;
			check(a,l,test);
		}
		else
		{
			a[0]=9;
			int prev=0;
			
			for (j=1;j<l;j++)
			{
				if (a[j]!=0 && prev==0)
				{
					a[j]=a[j]-1;
					prev=1;
					break;
				}
				else if(a[j]==0 && prev==0)
				{
					a[j]=9;
					prev=0;
				}
			}
			if (a[l-1]==0)
			{
				a[l-1]='\n';
				l=l-1;
			}
			check(a,l,test);
		}
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n;
		scanf("%d",&n);
		int a[2000];
		int p=n;
		int j=0;
		while(p>0)
		{
			int rem=p%10;
			a[j]=rem;
			j++;
			p=p/10;
		}
		a[j]='\n';
		check(a,j,i);
	}
}
