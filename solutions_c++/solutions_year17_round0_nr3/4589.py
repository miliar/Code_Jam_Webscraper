#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e6+10;

int t,k,n,x,a,b;

bitset <maxn> plansza;
priority_queue <int, vector<int>, less<int> > Q;

int main()
{
	scanf("%d",&t);
	for(int l=1;l<=t;l++)
	{
		scanf("%d%d",&n,&k);
		while(!Q.empty()) Q.pop();
		Q.push(n);
		for(int i=0;i<k;i++)
		{
			x = Q.top();
			Q.pop();
			a = x/2 - (x+1)%2;
			b = x/2;
			Q.push(a);
			Q.push(b);
		}
		cout << "Case #" << l << ": " << max(a,b) << " " << min(a,b) << endl;
	}
}
