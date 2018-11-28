// =============================================================================
// Author LUONG VAN DO
// Problem 
// Algorithm
// Time Limit
// =============================================================================
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <math.h>
#include <cstring>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

#define rep(i, n) for (int i=0;i<n;i++)
#define repr(i, n) for (int i = n - 1;i>=0;i--)
#define fr(i, a, b) for (int i=a;i<=b;i++)
#define frr(i, a, b) for (int i=b;i>=a;i--)
#define FileIn(file) freopen(file".inp", "r", stdin)
#define FileOut(file) freopen(file".out", "w", stdout)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 1000000009
#define N 1111
#define C 8888
#define md 1000000007
using namespace std;

inline long long max(long long a, long long b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Or(int mask, int bit) { return mask | (1 << bit); }
inline int Xor(int mask, int bit) { return mask ^ (1 << bit); }

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int cases, k;
char s[N];
bool checkDone(char str[]) {
	int len = strlen(str);
	rep(i, len) if (str[i] == '-') return false;
	return true;
}
int main() {
	#ifndef ONLINE_JUDGE
        freopen("exam.inp","r", stdin);
        freopen("exam.out","w", stdout);
    #endif
    scanf(" %d ", &cases);
    rep(i, cases) {
    	scanf("%s%d ", s, &k);
    	int len = strlen(s);
    	int ans = 0;
    	rep(i, len - k + 1) {
    		if (s[i] == '-') {
    			ans++;
    			fr(j, i, i + k - 1)
    				if (s[j] == '-') s[j] = '+';
    				else s[j] = '-';
    		}
    	}
    	if (checkDone(s)) printf("Case #%d: %d\n", i + 1, ans);
    	else printf("Case #%d: IMPOSSIBLE\n", i + 1);
    }
}