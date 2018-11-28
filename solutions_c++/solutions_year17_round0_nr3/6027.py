#include<queue>
#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

priority_queue<int> q[105];

int n,k;

int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("Cs.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n>>k;
		q[t].push(n);
		for(int i=1;i<k;i++)
		{
			int x = q[t].top()-1;
			q[t].pop();
			if(x%2==0) {q[t].push(x/2);q[t].push(x/2);}
			else {q[t].push(x/2);q[t].push(x/2+1);}
		}
		int x = q[t].top()-1;
		if(x%2==0)	printf("Case #%d: %d %d\n",t,x/2,x/2);
		else printf("Case #%d: %d %d\n",t,x/2+1,x/2);
	}
	return 0;
}
