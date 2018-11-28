#include<bits/stdc++.h>
using namespace std;
const int MAX=1e3+2;
double pi=M_PI;
struct souvik
{
	int r,h;
}p[MAX];
int tree[4*MAX+4];
bool comp(souvik a,souvik b)
{
	return 	1LL*a.r*a.h > 1LL*b.r*b.h;
}
void build(int node, int start, int end)
{
    if(start == end) tree[node] = p[start].r;
    else
    {
        int mid = (start + end) / 2;
        build(2*node+1, start, mid);
        build(2*node+2, mid+1, end);
        tree[node] =max(tree[2*node+2],tree[2*node+1]);
    }
}
int query(int node, int start, int end, int l, int r)
{
    if(r < start or end < l) return 0;
    if(l <= start and end <= r)   return tree[node];
    int mid = (start + end) / 2;
    int p1 = query(2*node+1, start, mid, l, r);
    int p2 = query(2*node+2, mid+1, end, l, r);
    return max(p1,p2);
}
int main()
{
	int n,k,i,j,t,c,no=0;
	double inter,ans=0.0,x=0.0;
	scanf("%d",&t);
	while(t--)
	{
		no++;
		ans=0.0;
		x=0.0;
		scanf("%d %d",&n,&k);
		for(i=0;i<n;i++) scanf("%d %d",&p[i].r,&p[i].h);
		sort(p,p+n,comp);
		for(i=0;i<k;i++) x=x+1.0*p[i].r*p[i].h;
		build(0,0,n-1);
		for(i=0;i<n;i++)
		{
				inter=2.0*pi*x;
				c=k-1;
				if(i>=k) inter-=2.0*pi*p[k-1].r*p[k-1].h-2.0*pi*p[i].r*p[i].h,c--;
				int mr=query(0,0,n-1,0,c);
				mr=max(mr,p[i].r);
				inter+=pi*(1.0*mr*mr);
				if(inter>ans) ans=inter;
		}
		printf("Case #%d: %.7lf\n",no,ans);
	}
	return 0;
}