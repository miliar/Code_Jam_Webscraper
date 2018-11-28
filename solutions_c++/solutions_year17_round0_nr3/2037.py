#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<utility>
#include<map>
#include<set>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define REP(i,a,b) for(int i=a; i<=b; ++i)
#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define MP make_pair
#define sf scanf
#define pf printf
typedef long long LL;
typedef pair<int,int> pii;

map<LL,LL> Map;
priority_queue<LL> que;

int main()
{
	int T;
	LL n, kk, mx, mi;
	sf("%d", &T);
	REP(t,1,T)
	{
		sf("%lld%lld", &n, &kk);
		Map.clear();
		while(!que.empty()) que.pop();
		Map[n] = 1, que.push(n);
		while(!que.empty())
		{
			LL tn = que.top();
			LL cont = Map[tn];
			que.pop(), Map.erase(tn);
			LL ll = (tn-1)/2, rr = tn-1 - ll;
			if(cont >= kk)
			{
				mx = max(ll, rr);
				mi = min(ll, rr);
				break;
			}
			kk -= cont;

			if(!Map.count(ll))
			{
				Map[ll] = cont;
				que.push(ll);
			}
			else Map[ll] += cont;

			if(!Map.count(rr))
			{
				Map[rr] = cont;
				que.push(rr);
			}
			else Map[rr] += cont;
		}
		printf("Case #%d: %lld %lld\n", t, mx, mi);
	}
	return 0;
}
