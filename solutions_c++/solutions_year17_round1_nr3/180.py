#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define LOOP(i, v) for(int i = 0; i < v.size(); i++)
#define EPS 1e-9
#define INF 1e12
#define debug(x) cerr << "DEBUG : " << (#x) << " => " << (x) << endl

map<int, int> memo;
map<int, bool> encours;
int Hd, Ad, Hk, Ak, B, D;


int dp(int hd, int ad, int hk, int ak)
{
	if(hd < 0) hd = 0;
	if(hk < 0) hk = 0;
	int val = ak+101*hk+101*101*ad+101*101*101*hd;
	if(memo[val]) return memo[val]-1;
	if(hk <= 0)
	{
		memo[val] = 1;
		//fprintf(stderr, "%d %d %d %d --> %d\n", hd, ad, hk, ak, 1);
		return 0;
	}
	else if(hd <= 0)
	{
		memo[val] = 1000000001;
		//fprintf(stderr, "%d %d %d %d --> %d\n", hd, ad, hk, ak, 1000000000);
		return 1000000000;
	}
	if(encours[val])
	{
		//fprintf(stderr, "%d %d %d %d --> %d\n", hd, ad, hk, ak, 1000000000);
		return 1000000000;
	}
	encours[val] = true;
	int poss = 1000000000;
	poss = min(poss, 1+dp(hd-ak, ad, hk-ad, ak));
	poss = min(poss, 1+dp(hd-ak, min(ad+B,100), hk, ak));
	poss = min(poss, 1+dp(Hd-ak, ad, hk, ak));
	int newak = max(ak-D, 0);
	poss = min(poss, 1+dp(hd-newak, ad, hk, newak));
	memo[val] = poss+1;
	encours[val] = false;
	//fprintf(stderr, "%d %d %d %d --> %d\n", hd, ad, hk, ak, poss);
	return poss;
}

int main()
{
	int T;
	scanf("%d\n", &T);

	REP(t, 1, T)
	{
		fprintf(stderr, "Cas %d\n", t);
		printf("Case #%d: ", t);
		memo.clear();
		encours.clear();
		scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		//fprintf(stderr, "%d %d %d %d\n", Hd, Ad, Hk, Ak);
		int rep = dp(Hd, Ad, Hk, Ak);
		if(rep == 1000000000) printf("IMPOSSIBLE\n");
		else printf("%d\n", rep);
		//fprintf(stderr, "%d\n", rep);
	}
	
	return 0;
}
