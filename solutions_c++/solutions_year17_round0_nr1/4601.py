#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define si(a) scanf("%d ",&a);
#define si2(a,b) scanf("%d %d ",&a,&b);
#define si3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sll(a) scanf("%lld ",&a);
#define sll2(a,b) scanf("%lld%lld",&a,&b)
#define sll3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sf(a) scanf("%f ",&a);
#define sd(a) scanf("%lf ",&a);
#define sc(a) scanf("%c ",&a);
#define ss(a) scanf("%s ",a);
#define sf2(a,b) scanf("%f %f ",&a,&b);
#define sd2(a,b) scanf("%lf %lf ",&a,&b);
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define all(a) a.begin(),a.end()
#define forn(i,n) for(int i=0;i<n;i++)
#define forq(i,q,n) for(int i=q;i<n;i++)
#define form(i,n) for(int i=n;i>=0;i--)
#define forp(i,q,n) for(int i=q;i>=n;i--)
#define fi first
#define se second
#define INF 1000000010
#define MOD 1000000007
#define MAXN
#define LL long long int

char s[1234];

void init()
{
	int t = 1, T;
	si(T);
	while(t <= T)
	{
		printf("Case #%d: ", t);
		int k;
		cin >> s >> k;
		int l = strlen(s);
		list <int> L;
		int cnt = 0;
		for (int i = 0; i < l; ++i)
		 {
		 	while(!L.empty() && L.front() < i)
		 	{
		 		L.pop_front();
		 	}
		 	int ls = L.size();
		 	if(((s[i] == '-') + ls) % 2 == 0)
		 	{
		 		continue;
		 	}
		 	cnt++;
		 	L.push_back(i + k - 1);
		 }

		 if(L.empty() || L.back() < l) {
		 	printf("%d\n", cnt);
		 } 
		 else 
		 {
		 	printf("IMPOSSIBLE\n");
		 }
		t++;
	}
}

int main()
{

	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif

	init();

	return 0;
}