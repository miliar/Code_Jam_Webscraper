#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <queue>

using namespace std;

int n,k;

struct node
{
	int a,len;	
	friend bool operator<(node x,node y)
	{
		if(x.len==y.len)
			return x.a>y.a;
		return x.len<y.len;
	}
};

void solve()
{
	int T=k;
	priority_queue<node> Q;
	while(!Q.empty())
		Q.pop();
	node q,tmp;
	q.a=1; q.len=n;
	Q.push(q);
	while(T--)
	{
		q=Q.top();
		Q.pop();
		tmp.len=(q.len-1)/2;
		tmp.a=q.a;
		q.a=tmp.a+tmp.len+1;
		q.len=q.len-1-tmp.len;
		if(q.len>0)
			Q.push(q);
		if(tmp.len>0)
			Q.push(tmp);
	}
	int mx=max(q.len,tmp.len),mn=min(q.len,tmp.len);
	printf("%d %d\n",mx,mn);
}

int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
	int T,cas=0;
	cin>>T;
	while(T--)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",++cas);
		solve();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
