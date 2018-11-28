#include <bits/stdc++.h>
using namespace std;

#define pb push_back

int n,p,cnt[5];
map <vector <int>,int> f;

int dfs(vector <int> v)
{
	if (f.find(v)!=f.end())
		return f[v];
	int ans=0;
	for (int i=1;i<p;i++)
	{
		v[i-1]++;
		if (v[i-1]>cnt[i])
		{
			v[i-1]--;
			continue;
		}
		int t=dfs(v),sum=0;
		for (int j=1;j<p;j++)
			sum+=j*(cnt[j]-v[j-1]);
		if (sum%p==0)
			t++;
		ans=max(ans,t);
		v[i-1]--;
	}
	f[v]=ans;
	return ans;
}

void solve()
{
	scanf("%d%d",&n,&p);
	memset(cnt,0,sizeof(cnt));
	for (int i=0;i<n;i++)
	{
		int g;
		scanf("%d",&g);
		cnt[g%p]++;
	}
	vector <int> v;
	f.clear();
	for (int i=1;i<p;i++)
		v.pb(cnt[i]);
	f[v]=0;
	for (int i=0;i+1<p;i++)
		v[i]=0;
	int ans=dfs(v);
	ans+=cnt[0];
	printf("%d\n",ans);
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
