#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,x;
	FILE *fip,*fop;
	fip=fopen("B-small-attempt1.in","r");
	fop=fopen("ans.out","w");
	fscanf(fip,"%d",&t);
	for(x=0;x<t;x++)
	{
		long long int i,j,asd;
		fscanf(fip,"%lld",&i);
		asd=i;
		abc:
		int a[20],b[20];
		long long int temp=asd,k=0,c;
		while(temp>0)
		{
			a[k]=temp%10;
			k++;
			temp/=10;
		}
		c=k;
		while(true)
		{
			for(k=0;k<c-1;k++)
				if(a[k]<a[k+1])
					break;
		/*	printf("k=%lld\n",k);
				for(j=c-1;j>=0;j--)
					printf("%d ",a[j]);
		*/	if(k==c-1)
			{
				fprintf(fop,"Case #%d: ",x+1);
				for(j=c-1;j>=0;j--)
					fprintf(fop,"%d",a[j]);
				fprintf(fop,"\n");
				break;
			}
			else
			{
		//		printf("in else");
				a[k+1]--;
				for(j=0;j<=k;j++)
					a[j]=9;
				if(a[c-1]==0)
				{
					asd--;
		//			printf("asd ");
					goto abc;
				}
			}
		}
	}
	return 0;
}
