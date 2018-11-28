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

int t, n, k, a, b, now;

priority_queue <pair <int, pii>, vector < pair <int, pii> >, greater <pair <int, pii>> > S;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	
	while (t--) {
		scanf("%d%d", &n, &k);
		
		S.push({-n, {1, n+2}});
		
		FOR (i, 1, k) {
			pair <int, pii> T = S.top();
			
			S.pop();
			
			int N = -T.ff;
			int l = T.ss.ff;
			int r = T.ss.ss;
			
//			cout << N << ": " << l << " " << r << "\n";
			
			int j = (N+1)/2;
			
			if (1-j != 0)
			S.push({1-j, {l, l+j}});
			if (-r+l+j+1!=0)
			S.push({-r+l+j+1, {l+j, r}});
			
			if (N&1)
				a = b = N/2;
			else
				a = N/2, b = N/2-1;
		}
		
		while (!S.empty())
			S.pop();
		
		printf("Case #%d: %d %d\n",++now, a, b);
	}
}

