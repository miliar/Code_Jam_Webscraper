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

int t, l , L;
char s[123];

void change(int );
void notchange(int );

void init()
{
	si(t);
	int T = 1;
	while(T <= t)
	{
		printf("Case #%d: ", T);
		
		ss(s + 1);
		//printf("%s\n", s);
		l = strlen(s + 1);
		L = strlen(s + 1);
		//printf("%c\n", s[l- 1]);
		int ck = l;
		//ck = 1;
		while(ck)
		{
			if(s[ck] < s[ck - 1])
			{
				change(ck - 1);
				notchange(ck);
			}
			ck--;
		}
		printf("%s\n", s  + 1 + (s[1] == '0'));
		T++;
	}
}

void notchange (int x) {
	while(x <= L) 
	{
		s[x] = '9'; x += 1;
	}
}

void change (int x)
{
	while(x && (s[x] == '0'))
	{
		s[x] = '9'; x -= 1;
	}
	s[x]--;// -= 1;
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