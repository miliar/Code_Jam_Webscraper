#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
double pi=3.141592653589793;
struct node
{
	double r,h;
	int index;
};
struct node p[10001],copyy[10001];
inline bool comp1(node p1,node p2)
{
	return (2*pi*p1.r*p1.h)>(2*pi*p2.r*p2.h);
}
int main()
{
	
	int viv=0;
	int t;
	scanf("%d",&t);
	while(t--)
	{
		double fin=0;
		int n,k,i;
		viv++;
		printf("Case #%d: ",viv);
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++)
		{
			cin>>p[i].r>>p[i].h;
			p[i].index=i;
			copyy[i].r=p[i].r;
			copyy[i].h=p[i].h;
			copyy[i].index=p[i].index;
		}
		sort(copyy,copyy+n,comp1);
		int test=0;
		while(test<n){
		double ans=(pi*p[test].r*p[test].r)+(2*pi*p[test].r*p[test].h);
		int cnt=1;
		for(i=0;i<n;i++)
		{
			if(cnt==k)break;
			if(copyy[i].index==p[test].index)continue;
			if(copyy[i].r>p[test].r)continue;
			cnt++;
			ans=ans+(2*pi*copyy[i].r*copyy[i].h);
		}
		test++;
		if(cnt==k)
		fin=max(fin,ans);
		}
		printf("%0.09lf",fin);
		printf("\n");
	}
}