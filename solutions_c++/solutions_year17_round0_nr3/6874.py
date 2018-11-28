#include <iostream>
#include <queue>
using namespace std;
typedef long long LL;
const int N = 1000005;

#define BUG

int n,m;
int s[N];

int main()
{

#ifdef BUG
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.txt","w",stdout);
#endif
	
	int cc,kk;
	scanf("%d",&kk);
	for (int cc=1;cc<=kk;cc++)
	{
		scanf("%d%d",&n,&m);
		priority_queue <int> q;
		q.push(n);
		for (int i=0;i<m-1;i++)
		{
			int x=q.top();
			int a=x/2,b=x-x/2-1;
			q.pop();
			q.push(a);
			q.push(b);
		}
		int x=q.top();
		int a=x/2,b=x-x/2-1;
		printf("Case #%d: %d %d\n",cc,max(a,b),min(a,b) );
	}
	return 0;
}
/*

5
4 2
5 2
6 2
1000 1000
1000 1

*/
