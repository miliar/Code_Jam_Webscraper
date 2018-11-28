#include <cstdio>
#include <cstring>
#include <algorithm>

int t,n,m;
int resp[100];
int pack[100][100];
int pos[100],maxs[100],mins[100];

int maxserv(int i)
{
	int r=resp[i],p=pack[i][pos[i]];
	int res = (p*10) / (r*9); /* p/(r*9/10) */ 
	//while((r*9)*res>(p*10))--res;
	return res;
}

int minserv(int i)
{
	int r=resp[i],p=pack[i][pos[i]];
	int res = (p*10) / (r*11); /* p/(r*11/10) */ 
	while((r*11)*res<(p*10))++res;
	return res;
}

bool inc(int i, bool& flag)
{
	if(flag)
	{
		++pos[i];
		if(pos[i]==m)
			flag=false;
		else
		{
			maxs[i]=maxserv(i);
			mins[i]=minserv(i);
		}
	}
	return flag;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int c=0;c<t;++c)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			scanf("%d",&resp[i]);
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				scanf("%d",&pack[i][j]);
		memset(pos,0,sizeof(pos));
		for(int i=0;i<n;++i)
			std::sort(pack[i],pack[i]+m);
		for(int i=0;i<n;++i)
		{
			maxs[i]=maxserv(i);
			mins[i]=minserv(i);
		}
		bool flag=true;
		int res=0;
		while(flag)
		{
			int li=std::max_element(mins,mins+n)-mins;
			int ri=std::min_element(maxs,maxs+n)-maxs;
			if(mins[li]>maxs[ri])
				inc(ri,flag);
			else 
			{
				res+=1;
				for(int i=0;i<n;++i)
					inc(i,flag);
			}
		}
		printf("Case #%d: %d\n",c+1,res);
	}
	return 0;
}


