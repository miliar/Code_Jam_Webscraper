#include<bits/stdc++.h>
using namespace std;
struct node
{
	int first;
	int second;
};
bool operator<(node a,node b)
{
	int x=a.second-a.first;
	int y=b.second-b.first;
	if(x!=y)
		return x<y;
	return a.first > b.first;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cnt=1;cnt<=t;cnt++)
	{
		int k,n;
		scanf("%d %d",&n,&k);
		priority_queue< node >q;
		q.push((node){1,n+2});
		while(!q.empty() && k > 0)
		{
			node p=q.top();
			q.pop();
			int pos=(p.first+p.second)/2;
			if(k==1)
			{
				int ls,rs;
				ls=pos-p.first-1;
				rs=p.second-pos-1;
				printf("Case #%d: %d %d\n",cnt,max(ls,rs),min(ls,rs));
				break;
			}
				q.push((node){pos,p.second});
				q.push((node){p.first,pos});	
		//	}
			k--;

		}
	}
	return 0;
}