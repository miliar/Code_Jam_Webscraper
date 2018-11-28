#include <set>
#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string.h>
#include <limits.h>
#include <algorithm>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
//#include <bits/stdc++.h>

#define ff first
#define ss second
#define ll long long
#define pb push_back
#define mp make_pair
#define inf 1000000007
#define mod 1000000007
#define pii pair <int, int>
#define all(x) x.begin(), x.end()
#define FOR(i, x, y) for (int i = x; i <= y; i++)
//#define tr(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

//using namespace __gnu_pbds;

using namespace std;

//template <typename T> using ordered_set =  tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

ll n, ans;

int now, t;

ll F(ll x, int y) {
	if (x > n)
		return 0;
	
	ans = max(ans, x);
	for (int i = y; i <= 9; i++) {
		if (x==0&&i==0)
			continue;
		F(x*10LL+i, i);
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	while (t--) {
		scanf("%lld", &n);
		ans=0;
		F(0, 0);
		printf("Case #%d: %lld\n",++now,  ans);
	}
}

