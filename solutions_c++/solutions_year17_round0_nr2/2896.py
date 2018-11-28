#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <numeric>
#include <cassert>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <ctime>

using namespace std;

#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))
#define EPS 1e-9
typedef long long LL;
const LL MOD = 1e9 + 7;
const int INF = 1e9 + 1;

int main(int argc, char** argv) {
#ifdef HOME
	freopen("B-large.in", "rb", stdin);
	freopen("B-large.out", "wb", stdout);
#endif
	int T;
	scanf("%d", &T);
	FOR(tc, 1, T + 1)
	{
		LL N;
		scanf("%lld", &N);
		vector<int> v;
		while (N)
		{
			v.push_back(N % 10);
			N /= 10;
		}
		reverse(v.begin(), v.end());
		int idx = 0;
		while (idx < v.size() - 1)
		{
			if (v[idx] <= v[idx + 1])
			{
				++idx;
			}
			else
			{
				--v[idx];
				for(int i = idx + 1; i < v.size(); ++i)
				{
					v[i] = 9;
				}
				--idx;
			}
		}
		LL res = 0;
		REP(i, v.size())
		{
			res *= 10;
			res += v[i];
		}
		printf("Case #%d: %lld\n", tc, res);
	}
	
	return 0;
}
