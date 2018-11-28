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

int T;
ll n;

ll ones[20]; // 1, 11, 111, ...

int main(int argc, const char * argv[])
{
	scanf("%d", &T);
	ones[0] = 1;
	for (int i = 1; i <= 18; ++i) {
		ones[i] = ones[i - 1] * 10LL + 1LL;
	}

	for (int tc = 0; tc < T; ++tc) {
		scanf("%lld", &n);

		int log;
		for (log = 0; log <= 18; ++log) {
			if (ones[log] > n) {
				--log;
				break;
			}
		}

		ll x = 0;

		int rem = 0;
		while (log >= 0) {
			while (n >= x && rem <= 9) {
				++rem;
				x += ones[log];
			}
			x -= ones[log];
			--rem;
			--log;
		}

		printf("Case #%d: %lld\n", tc + 1, x);
	}

	return 0;
}