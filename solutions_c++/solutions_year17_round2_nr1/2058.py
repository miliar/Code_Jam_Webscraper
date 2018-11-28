#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <cassert>
#include <cmath>

#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <string>
#include <iterator>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <array>
#include <map>
#include <set>
#include <deque>
#include <set>
#include <unordered_set>
#include <unordered_map>

//#include<bits/stdtr1c++.h>

#define fi first
#define se second
#define inf 2147483647
#define mod 1000000009

#define mset(a, s) memset(a, s, sizeof(a))
#define forall(i,a,b) for(int i=a;i<b;++i)
#define max(a, b) (a < b ? b : a)
#define min(a, b) (a > b ? b : a)
#define all(a) a.begin(), a.end()
#define len(a) sizeof a/sizeof a[0]

/*/ --remove first * or add / before to enable scan--
#define scan(x) do{while((x=getchar())<0); for(x-='0';(_=getchar())>='0';x=(x<<3)+(x<<1)+_-'0');}while(0);
char _;//*/

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

ll T, d, n;
ll k[1005], s[1005];

int main(int argc, const char * argv[])
{
	scanf("%lld", &T);
	for (int tc = 0; tc < T; ++tc) {

		scanf("%lld%lld", &d, &n);
		double ans = -1;

		for (int i = 0; i < n; ++i) {
			scanf("%lld%lld", &k[i], &s[i]);
			double vr = (double)d * s[i] / (d-k[i]);
			//vr = max(vr, s[i]);
			if (ans < 0) ans = vr;
			else ans = min(ans, vr);
		}

		//printf("Case #%d: IMPOSSIBLE\n", tc + 1);
		printf("Case #%d: %.6lf\n", tc + 1, ans);
	}

	return 0;
}