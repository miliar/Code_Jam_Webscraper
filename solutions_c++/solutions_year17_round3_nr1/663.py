/*
prob: Codejam17-1C-A
id: amlansaha
lang: C++
date: 2017-04-30
algo: Sort, DP
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef vector<int> VI;
typedef vector<long long> VLL;
typedef map<int, int> MAPII;
typedef map<string,int> MAPSI;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef double LD;
typedef pair<LD,LD> PDD;

#define FOR(i,a,b) for(i=a;i<=b;i++)
#define ROF(i,a,b) for(i=a;i>=b;i--)
#define FR(i,n)    for(i=0;i<n;i++)
#define RF(i,n) for(i=n;i>0;i--)
#define CLR(a) memset ( a, 0, sizeof ( a ) )
#define RESET(a) memset ( a, -1, sizeof ( a ) )
#define PB(a)    push_back ( a )
#define R first
#define H second

const int INF = 2000000009;
const int Max = 1007;
const double PI = acos(-1.0);

vector<PLL>inp;

LL dpTab[Max][Max];
LL ANS;

LL rec(int pos, int rem)
{
	if(pos<0||rem==0)	return 0;
	LL &ret = dpTab[pos][rem];
	if(ret>-1)	return ret;

	ret = rec(pos-1,rem-1)+2*inp[pos].R*inp[pos].H;
	ANS = max(ret+inp[pos].R*inp[pos].R, ANS);
	LL temp = rec(pos-1,rem);
	ret = max(ret,temp);
	return ret;
}

int main ()
{
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
	int i,j,k,l,m,n,t, caseno=0;
	double temp, ans;
	LL r,h;

	scanf ( "%d", &t);

	while(t--)	{
		scanf ( "%d %d", &n, &k);
		inp.clear();
		FR(i,n)	{
			cin>>r>>h;
			inp.push_back(make_pair(r,h));
		}
		sort(inp.begin(),inp.end());
		RESET(dpTab);
		ANS = 0;

		rec(n-1,k);
		ans = ((double)ANS)*PI;
		printf ( "Case #%d: %.10lf\n", ++caseno, ans);
	}

	return 0;
}