#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<queue>
using namespace std;
typedef long long LL;
priority_queue<LL>q;
int n, k, T;
int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		scanf("%d%d", &n, &k);
		int a, b;
		q.push(0);
		q.push(n);
		while(k--)
		{
			LL temp = q.top();
			q.pop();
			a = (temp - 1) / 2;
			b = temp - a - 1;
			q.push(a);
			q.push(b);
		}
		printf("Case #%d: %d %d\n", i, max(a, b), min(a, b));
		while(!q.empty())q.pop();
	}
}
