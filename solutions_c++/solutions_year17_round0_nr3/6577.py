#include <bits/stdc++.h>

using namespace std;
const int maxn=1e3;

struct Pair
{
	int lv;
	int rv;
	int pos;
	
	bool operator < (const Pair& rhs) const
	{
		if (min(lv,rv)!=min(rhs.lv,rhs.rv)) return min(lv,rv)<min(rhs.lv,rhs.rv);
		else if (max(lv,rv)!=max(rhs.lv,rhs.rv)) return max(lv,rv)<max(rhs.lv,rhs.rv);
		else return pos>rhs.pos;
	}
};


int n,k;
vector <Pair> v;
bool vis[maxn+5];

void solve(int iCase)
{
	v.clear();
	memset(vis,0,sizeof(vis));
	
	for (int i=1;i<=n;++i)
	{
		auto p=(Pair){i-1,n-i,i};
		v.push_back(p);
	}
	
	Pair tmp;
	for (int j=1;j<=k;++j)
	{
		tmp=(Pair){0,0,n+1};
		for (int i=0;i<n;++i)
		{
			if (!vis[i]) tmp=max(tmp,v[i]);
		}
		
		int pos=tmp.pos;
		vis[tmp.pos-1]=true;
		for (int i=0;i<n;++i)
		{
			if (v[i].pos==pos) continue;
			else if (v[i].pos>pos)
			{
				v[i].lv=min(v[i].lv,v[i].pos-pos-1);
			}
			else
			{
				v[i].rv=min(v[i].rv,pos-v[i].pos-1);
			}
		}
		/*
		for (int i=0;i<n;++i)
		{
			printf("j=%d,lv=%d,rv=%d,pos=%d\n",j,v[i].lv,v[i].rv,v[i].pos);
		}
		*/
	}
	
	printf("Case #%d: %d %d\n",iCase,max(tmp.lv,tmp.rv),min(tmp.lv,tmp.rv));
}

int main(void)
{
	#ifdef ex
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	#endif
	
	int T;
	scanf("%d",&T);
	for (int iCase=1;iCase<=T;++iCase)
	{
		scanf("%d%d",&n,&k);
		solve(iCase);
	}
}
