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

int t, n, k, now;

char s[1005];

void upd(int l, int r) {
	FOR (i, l, r)
		s[i]=(s[i]=='-'?'+':'-');
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	
	while (t--) {
		scanf("%s", s);
		scanf("%d", &k);
		
		n = strlen(s);
		
		int j = 0;
		for (int i = n-1; i >= 0; i--) {
			if (s[i] == '-' && i-k+1 >= 0)
				upd(i-k+1, i), j++;
		}
		
		FOR (i, 0, n-1)
			if (s[i] == '-')
				j = -1;
		
		printf("Case #%d: ", ++now);
		
		if (j != -1)
			printf("%d\n", j);
		else
			printf("IMPOSSIBLE\n");
	}
}

