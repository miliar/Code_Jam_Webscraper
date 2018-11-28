#include <stdio.h>
#include <algorithm>

#define DAY (60*24)
#define HALF (60*12)

FILE* in=fopen("B-large.in","r");
FILE* out=fopen("B-large.out","w");

struct INTERVAL
{
	int s,f,t;
	void get(int _t)
	{
		fscanf(in,"%d %d",&s,&f);
		t=_t;
	}
	bool operator<(const INTERVAL& I) const
	{
		return s<I.s;
	}
}I[200];

void solve()
{
	int i,j,a,b,n;
	fscanf(in,"%d %d",&a,&b);
	for(i=0;i<a;i++)
		I[i].get(0);
	for(i=0;i<b;i++)
		I[i+a].get(1);
	
	n=a+b;
	std::sort(I,I+n);
	
	int t,m[2]={};
	int d[2][200]={};
	int pos[2]={HALF,HALF};
	int ans=0;
	
	for(i=0;i<n;i++)
	{
		t=I[i].t;
		if(t==I[(i+1)%n].t)
			d[t][m[t]++]=(I[(i+1)%n].s-I[i].f+DAY)%DAY;
		else ans+=1;
		pos[t]-=I[i].f-I[i].s;
	}
	
	for(i=0;i<2;i++)
	{
		std::sort(d[i],d[i]+m[i]);
		for(j=0;j<m[i];j++)
		{
			if(d[i][j]>pos[i])
			{
				ans+=2*(m[i]-j);
				break;
			}
			pos[i]-=d[i][j];
		}
	}
	fprintf(out,"%d\n",ans);
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
