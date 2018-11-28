#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <numeric>
#include <cassert>
#include <cmath>
#include <map>
#include <unordered_map>
#include <set>


using namespace std;
typedef unsigned int uint;
typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef vector<VL> VVL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef vector<PII > VPII;
typedef vector<VPII> VVPII;

#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))
int main(int argc, char** argv) {
#ifdef HOME
	freopen("B-small-attempt1.in", "rb", stdin);
	freopen("B-small-attempt1.out", "wb", stdout);
	freopen("err.txt", "wb", stderr);
#endif
	int T,N,R,O,Y,G,B,V;
	scanf("%d", &T);
	FOR(tc, 1, T + 1)
	{
		scanf("%d %d %d %d %d %d %d", &N, &R,&O,&Y,&G,&B,&V);
		//R,Y -> O
		//Y,B -> G
		//R,B, -> V
		//
		int r = R + O + V;
		int y = Y + O + G;
		int b = B + G + V;
		if (2 * r > N || 2 * y > N || 2 * b > N)
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		string rs("ROYGBV");
		int n[6] = { 4,6,2,3,1,5 };
		int v[6];
		v[0] = R, v[1] = O, v[2] = Y, v[3] = G, v[4] = B, v[5] = V;

		string res;
		while (N)
		{
			int rr = v[0] + v[1] + v[5];
			int yy = v[1] + v[2] + v[3];
			int bb = v[4] + v[5] + v[3];
			--N;
			REP(i, 6) if(v[i])
			{
				int actmask = n[i];
				//can choose 
				bool ok = 1;
				int j = -1;
				if (res.size())
				{
					REP(k, 6)
						if (rs[k] == res.back())
							j = k;
					if (n[j] & n[i])
						ok = false;
				}
				//what would be the r,y,b
				if(!ok)
					continue;
				int yyy = yy, rrr = rr, bbb =bb;
				if (i == 0)
					--rrr;
				if (i == 1)
					--rrr, --yyy;
				if (i == 2)
					--yyy;
				if (i == 3)
					--bbb, --yyy;
				if (i == 4)
					--bbb;
				if (i == 5)
					--rrr, --bbb;
				if (rrr <= yyy + bbb && yyy <= rrr + bbb && bbb <= rrr + yyy)
				{
					//okay
					res += rs[i];
					v[i]--;
					break;
				}
				if (rrr - 1 == yyy + bbb && i != 0 && i!= 1 && i!=5)
				{
					//okay
					res += rs[i];
					v[i]--;
					break;
				}
				if (yyy - 1 == rrr + bbb && i != 1 && i != 2 && i != 3)
				{
					//okay
					res += rs[i];
					v[i]--;
					break;
				}

				if (bbb - 1 == rrr + yyy && i != 3 && i != 4 && i != 5)
				{
					//okay
					res += rs[i];
					v[i]--;
					break;
				}
			}
		}
		printf("Case #%d: %s\n", tc,res.c_str());
	}
	return 0;
}
