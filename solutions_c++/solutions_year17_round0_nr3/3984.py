#include<stdio.h>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<queue>
using namespace std;



int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int cas=1;
	while(T--)
	{
		int n,k;
		priority_queue<int>q;
		while(!q.empty())q.pop();
		printf("Case #%d: ",cas++);
		scanf("%d%d",&n,&k);
		q.push(n);
		int o=1;
		while(o<k)
		{
			int p=q.top()-1;
			q.pop();
			q.push(p/2);
			q.push(p-p/2);
			o++;
		}
		int u=q.top()-1;
		printf("%d %d\n",u-u/2,u/2);
	}
	return 0;
}
