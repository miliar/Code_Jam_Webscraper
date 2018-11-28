#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
using namespace std;
struct event
{
	int s, e, p;
	event(int a, int b, int c)
	{
		s = a;
		e = b;
		p = c;
	}
	bool operator <(const event & second) const
	{
		return s< second.s;
	}
};
int T;
int MOD = 24*60;
int main()
{
	freopen("infile.txt", "r", stdin);
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		int A, B;
		vector<event> V;
		scanf("%d %d", &A, &B);
		int hours[2]={0, 0};
		for(int a=0; a<A; a++)
		{
			int s, e;
			scanf("%d %d", &s, &e);
			V.push_back(event(s, e, 0));
			hours[0]+= e-s;
		}
		for(int b=0; b<B; b++)
		{
			int s, e;
			scanf("%d %d", &s, &e);
			V.push_back(event(s, e, 1));
			hours[1]+=e-s;
		}
		if(V.size()<=1)
		{
			printf("Case #%d: 2\n", t);
			continue;
		}
		sort(V.begin(), V.end());
		vector<int> extrahours[2];
		int ans = 0;
		for(int v=1; v<V.size(); v++)
		{ 
			if(V[v].p!= V[v-1].p) ans++;
			else
			{
				extrahours[V[v].p].push_back(V[v].s-V[v-1].e);
				hours[V[v].p]+= V[v].s-V[v-1].e;
			}
		}
		
		if(V[0].p!= V[V.size()-1].p) ans++;
		else
		{
			extrahours[V[0].p].push_back((V[0].s+MOD-V[V.size()-1].e)%MOD);
			hours[V[0].p]+= (V[0].s+MOD-V[V.size()-1].e)%MOD;
		}
		sort(extrahours[0].begin(), extrahours[0].end());
		sort(extrahours[1].begin(), extrahours[1].end());
		while (hours[0]>12*60 || hours[1]>12*60)
		{
			if(hours[0] > 12*60)
			{
				ans+=2;
				hours[0]-=extrahours[0].back();
				extrahours[0].pop_back();
			}
			if(hours[1] > 12*60)
			{
				ans+=2;
				hours[1]-=extrahours[1].back();
				extrahours[1].pop_back();
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}