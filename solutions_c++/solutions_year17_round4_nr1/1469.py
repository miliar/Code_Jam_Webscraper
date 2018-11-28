#include <stdio.h>

FILE* in=fopen("A-large.in","r");
FILE* out=fopen("A-large.out","w");


void solve()
{
	int n,i,t,p;
	int num[4]={};
	fscanf(in,"%d %d",&n,&p);
	for(i=0;i<n;i++)
	{
		fscanf(in,"%d",&t);
		num[t%p]++;
	}
	if(p==2)
	{
		fprintf(out,"%d\n",num[0]+(num[1]+1)/2);
	}
	else if(p==3)
	{
		t=num[1]<num[2]?num[1]:num[2];
		num[1]-=t;
		num[2]-=t;
		num[1]+=num[2];
		fprintf(out,"%d\n",num[0]+t+(num[1]+2)/3);
	}
	else
	{
		int ans=num[0];
		
		t=num[1]<num[3]?num[1]:num[3];
		num[1]-=t;
		num[3]-=t;
		num[1]+=num[3];
		ans+=t;
		
		t=num[1]/2<num[2]?num[1]/2:num[2];
		num[1]-=2*t;
		num[2]-=t;
		ans+=t;
		
		if(num[1]==0)
		{
			ans+=(num[2]+1)/2;
		}
		else if(num[2]==0)
		{
			ans+=(num[1]+3)/4;
		}
		else
		{
			ans+=(num[2]+1)/2+(num[2]%2==0);
		}
		
		fprintf(out,"%d\n",ans);
	}
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
