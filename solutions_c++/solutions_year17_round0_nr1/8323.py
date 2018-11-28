/*
_____/\\\\\\\________________________/\\\\\\\\\____________/\\\\\\\\\_
___/\\\/////\\\____________________/\\\\\\\\\\\\\_______/\\\////////__
__/\\\____\//\\\__________________/\\\/////////\\\____/\\\/___________
_\/\\\_____\/\\\___/\\\____/\\\__\/\\\_______\/\\\___/\\\_____________
_\/\\\_____\/\\\__\///\\\/\\\/___\/\\\\\\\\\\\\\\\__\/\\\_____________
_\/\\\_____\/\\\____\///\\\/_____\/\\\/////////\\\__\//\\\____________
_\//\\\____/\\\______/\\\/\\\____\/\\\_______\/\\\___\///\\\__________
__\///\\\\\\\/_____/\\\/\///\\\__\/\\\_______\/\\\_____\////\\\\\\\\\_
____\///////______\///____\///___\///________\///_________\/////////__
*/
#include <iostream>	
#include <time.h>
#include <vector>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <string.h>
#include <cstring>
#include <map>
#include <algorithm>
#include <bitset>
#include <queue>
#include <set>
#include <time.h>
#include <assert.h>
#include <sstream>
//#include <unordered_map>
#include <bitset>
#include <utility>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <numeric>
#include <math.h>
#include <cmath>
#include <complex>
#include <numeric>
#include <iomanip>
#if !ONLINE_JUDGE
#include "inc.h"
#endif
using namespace std;
typedef long long ll;

int k, dp[1 << 10], n;
char s[11];
int calc(int msk) {
	if((1 << n) - 1 == msk)
		return 0;
	auto &ret = dp[msk];
	if(ret == -1) {
		ret = 1 << 20;
		int x = (1 << k) - 1;
		ret = 1 + calc(msk^x);
		for(int i = k; i < n; ++i) {
			x |= 1 << i;
			x &= ~(1 << (i - k));
			ret = min(ret, 1 + calc(msk^x));
		}
	}
	return ret;
}

int main() {
#if !ONLINE_JUDGE
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
	decTime;
#endif

	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; ++T) {
		scanf("%s%d", s, &k);
		n = strlen(s);
		memset(dp, -1, sizeof dp);
		int msk = 0;
		for(int i = 0; i < n; ++i)
			if(s[i] == '+')
				msk |= 1 << (n - i - 1);
		printf("Case #%d: ", T);
		if(calc(msk) >= (1 << 20))
			puts("IMPOSSIBLE");
		else
			printf("%d\n", calc(msk));
	}


#if !ONLINE_JUDGE
	//printTime;
#endif
	return 0;
}