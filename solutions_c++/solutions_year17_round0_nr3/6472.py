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

int n, k;
struct node {
	int len, l, r;
	node() { }
	node(int len, int l, int r):len(len), l(l), r(r) { }
	inline bool operator<(const node &e)const {
		if(len == e.len){
			if(l == e.l)
				return r > e.r;
			return l > e.l;
		}
		return len > e.len;
	}
};


int main() {
#if !ONLINE_JUDGE
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
	decTime;
#endif

	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; ++T) {
		scanf("%d%d", &n, &k);
		set<node>st;
		st.insert(node(n, 1, n + 2));
		int l, r;
		while(k--) {
			node cur = *st.begin();
			st.erase(st.begin());
			if(cur.len & 1) {
				int mid = cur.l + cur.len / 2 + 1;
				st.insert(node(l = mid - cur.l - 1, cur.l, mid));
				st.insert(node(r = cur.r - mid - 1, mid, cur.r));
			} else {
				int mid = cur.l + cur.len / 2;
				st.insert(node(l = mid - cur.l - 1, cur.l, mid));
				st.insert(node(r = cur.r - mid - 1, mid, cur.r));
			}
		}
		printf("Case #%d: %d %d\n", T, max(l, r), min(l, r));
	}


#if !ONLINE_JUDGE
	//printTime;
#endif
	return 0;
}