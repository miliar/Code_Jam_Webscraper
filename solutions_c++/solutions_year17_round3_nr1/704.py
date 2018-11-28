#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const ld Pi = 3.14159265358979323846;
pair<int,int> cake[1003];
vector<ld> tmp;

int main()
{
	int T; scanf("%d", &T);
	for(int cas=1; cas<=T; ++cas) {
		int N, K; scanf("%d%d", &N, &K);
		for(int i=1;i<=N;++i)
			scanf("%d%d", &cake[i].X, &cake[i].Y);
		sort(cake+1, cake+N+1);
		ld ans = 0;
		for(int la=N; la>=K; --la) {
			ld res = Pi * cake[la].X * (cake[la].X + 2 * cake[la].Y);
			tmp.clear();
			for(int i=la-1; i>=1; --i)
				tmp.PB(2 * Pi * cake[i].X * cake[i].Y);
			sort(tmp.begin(), tmp.end());
			int sz = tmp.size();
			for(int i=1; i<K; ++i)
				res += tmp[sz-i];
			ans = max(ans, res);
		}
		printf("Case #%d: %.9Lf\n", cas, ans);
	}
	return 0;
}





