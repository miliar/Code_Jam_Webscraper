/*
prob: Codejam17-1C-B
id: amlansaha
lang: C++
date: 2017-04-30
algo: DP
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
#define CC 0
#define JJ 1

const int INF = 2000000009;
const int Max = 1007;
const double PI = acos(-1.0);

int responsible[1444];

int dpTab[1444][722][2];
int INIT;

int rec(int minNo, int cHas, int whoTakesCharge)
{
	// cout<<minNo<<" "<<cHas<<" "<<whoTakesCharge<<endl;
	if(minNo<0)	{
		if(cHas!=0)	return INF;
		else	return whoTakesCharge!=INIT;
	}
	if(cHas<0 || minNo<cHas-1)	return INF;

	if(responsible[minNo]!=-1)	{
		if(responsible[minNo]!=whoTakesCharge)	return INF;
	}

	int &ret = dpTab[minNo][cHas][whoTakesCharge];
	if(ret>-1)	return ret;

	ret = INF;

	// printf("%d %d %d\n", minNo,cHas,whoTakesCharge);
	if(whoTakesCharge==CC)	cHas--;
	ret = rec(minNo-1,cHas,JJ)+(whoTakesCharge!=JJ);
	ret = min(INF,ret);
	int temp = rec(minNo-1,cHas,CC)+(whoTakesCharge!=CC);
	ret = min(ret,temp);
	return ret;
}

int main ()
{
   // freopen("B-large.in", "r", stdin);
   // freopen("B-large.out", "w", stdout);
	int i,j,k,l,m,n,t, caseno=0;
	int temp, ans;
	LL r,h;

	scanf ( "%d", &t);
	int ac,aj;

	while(t--)	{
		RESET(responsible);
		RESET(dpTab);

		scanf ( "%d %d", &ac, &aj);

		FR(i,ac)	{
			scanf("%d %d", &j, &k);
			while(j<k)	{
				responsible[j]=CC;
				j++;
			}
		}
		FR(i,aj)	{
			scanf("%d %d", &j, &k);
			while(j<k)	{
				responsible[j]=JJ;
				j++;
			}
		}

		INIT = CC;
		ans = rec(1439,720,CC);

		RESET(dpTab);
		INIT = JJ;
		ans = min(ans,rec(1439,720,JJ));

		// ans = min(ans, rec(1439,720,JJ));
		printf ( "Case #%d: %d\n", ++caseno, ans);
	}

	return 0;
}

// 123
// 1 1
// 1439 1440
// 0 1

// 123
// 1 1
// 540 600
// 840 900
// 2 0
// 900 1260
// 180 540
// 1 1
// 1439 1440
// 0 1
// 2 2
// 0 1
// 1439 1440
// 1438 1439
// 1 2
// 3 4
// 0 10
// 1420 1440
// 90 100
// 550 600
// 900 950
// 100 150
// 1050 1400