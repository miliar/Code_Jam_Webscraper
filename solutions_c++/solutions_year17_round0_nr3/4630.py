#include<iostream>
#include<queue>
#include<cstdio>
using namespace std;
priority_queue<int> q;
int n,k,cas,now1,now2,T;
int main()
{
	freopen("c.out","w",stdout);
	cin>>T;
	while(T--)
	{
		while(q.size())
			q.pop();
		cin>>n>>k;
		q.push(n);
		while(k--)
		{
			int now=q.top();
			q.pop();
			q.push((now-1)/2);
			q.push((now)/2);
			now1=(now-1)/2;
			now2=(now)/2;
		}
		while(q.size()) q.pop();
		printf("Case #%d: %d %d\n",++cas,now2,now1);
	}
	return 0;
}
