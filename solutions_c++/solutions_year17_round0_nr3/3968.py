#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int n;
	cin>>n;
	for(int z=1;z<=n;z++)
	{
		priority_queue<int >que;
		int a,b;
		cin>>a>>b;
		que.push(a);
		while(--b)
		{
			int a1=que.top();
			que.pop();
			int c=(a1-1)/2;
			int d=(a1-1)-c;
			if(c!=0)
			que.push(c);
			if(d!=0)
			que.push(d);
		}
		int end=que.top();
		if(end&1)
		{
			printf("Case #%d: ",z);
			printf("%d %d\n",(end-1)/2,(end-1)/2);
		}
		else
		{
			printf("Case #%d: ",z);
			printf("%d %d\n",(end-1)/2+1,(end-1)/2);
		}
	}
	return 0;
}
