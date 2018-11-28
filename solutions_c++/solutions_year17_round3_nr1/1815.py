#include <bits/stdc++.h>
#define mp make_pair
#define ft first
#define sd second
#define ue printf("what?\n");
#define pb push_back
#define oo 0x3F3F3F3F
#define OO 0x3F3F3F3F3F3F3F3F
#define EPS 1e-9
#define inf 1000000000000000
#define maxn 200000
#define pi acos(-1)
#define N 200005
#define mod 1000000007
#define mdc __gcd

typedef long long ll;

using namespace std;

main()
{
	int t, caso, n, k, i, j, cont;
	pair<ll,pair<int,int> > v[1005];
	scanf("%d", &t);
	caso = 1;
	while(t--)
	{
		scanf("%d%d", &n, &k);
		for(i=0; i<n; i++)
			scanf("%d%d", &v[i].sd.sd, &v[i].sd.ft), v[i].ft = (ll)(2LL*v[i].sd.sd*v[i].sd.ft);
		sort(v,v+n);
		ll aux, ans = 0;
		for(i=n-1; i>=0; i--)
		{
			aux = (ll) v[i].sd.sd*v[i].sd.sd + v[i].ft;
			cont = 1;
			for(j=n-1; j>=0; j--)
			{
				if(j == i)
					continue;
				if(cont == k)
					break;
				if(v[j].sd.sd <= v[i].sd.sd)
					aux += (ll) v[j].ft, cont++;
			}
			ans = max(ans,aux);
		}
		printf("Case #%d: %.10lf\n", caso++, (double)ans*pi);
	}
}
			
				
		
