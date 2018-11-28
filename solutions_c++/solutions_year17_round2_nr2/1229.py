#include <stdio.h>
#include <algorithm>

FILE* in=fopen("B-small-attempt1.in","r");
FILE* out=fopen("B-small-attempt1.out","w");

char alpha[]=".ROYGBV";

struct INFO
{
	int ind,num;
	bool operator<(const INFO& I)const
	{
		return num>I.num;
	}
}info[7];

int c[7];
int ans[1000];

void solve()
{
	int i,j,k,n;
	fscanf(in,"%d",&n);
	for(i=1;i<=6;i++) fscanf(in,"%d",c+i);
	
	k=0;
	for(i=1;i<=6;i++)
	{
		if(2*c[i]>n)
		{
			fprintf(out,"IMPOSSIBLE\n");
			return;
		}
		info[i].ind=i;
		info[i].num=c[i];
	}
	
	std::sort(info+1,info+6+1);
	
	for(i=0;i<n;i++) ans[i]=0;
	
	k=1;
	for(i=0;i<n;i++)
	{
		j=(i*2);
		if(j>=n && n%2==0) j++;
		j%=n;
		
		while(c[info[k].ind]==0) k++;
		ans[j]=info[k].ind;
		c[info[k].ind]--;
	}
	for(i=0;i<n;i++)
		fprintf(out,"%c",alpha[ans[i]]);
	fprintf(out,"\n");
}

int main()
{
	int i,T;
	fscanf(in,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fprintf(out,"Case #%d: ",i);
		solve();
	}
}
