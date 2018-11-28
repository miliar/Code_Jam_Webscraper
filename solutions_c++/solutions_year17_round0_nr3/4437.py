#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n,k;
struct node
{
	int x;
	bool operator < (const node &a)const
	{
		return x<a.x;
	}
	node(){}
	node(int _x):x(_x){}
};
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int _=1;_<=T;_++)
	{
		priority_queue<node> Q;
		scanf("%lld%lld",&n,&k);
		Q.push(node(n));
		//Q.push(1);
		k--;
		while(k--)
		{
			node tmp=Q.top();
			Q.pop();
			tmp.x--;
			Q.push(node(tmp.x/2));
			Q.push(node(tmp.x-tmp.x/2));
		}
		node tmp=Q.top();
		tmp.x--;
		printf("Case #%d: ",_);
		printf("%d %d\n",tmp.x-tmp.x/2,tmp.x/2);
	}
	return 0;
}
