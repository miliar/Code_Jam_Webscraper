#include<bits/stdc++.h>
#define X first
#define Y second
using namespace std;
priority_queue<pair<int,int> > pq;
int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("output_C-small-2-attempt0.txt","w",stdout);
	int t,n,k,i,res,l,r,ll,rr,ct,num=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		res=0;
		while(!pq.empty()) pq.pop();
		pq.emplace(n-1,-1);
		while(k--)
		{
			l=-pq.top().Y;
			r=pq.top().X+l;
			pq.pop();
			res=(l+r)/2;
			ll=l;
			rr=r;
			if(l<=res-1) pq.emplace(res-1-l,-l);
			if(r>res) pq.emplace(r-(res+1),-(res+1));
		}
		printf("Case #%d: %d %d\n",num++,max(rr-res,res-ll),min(rr-res,res-ll));
	}

}