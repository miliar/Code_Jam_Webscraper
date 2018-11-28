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
#define INF 100005
#define N 100005
#define C 2
#define md 1000000007
#define eps 1e-6
using namespace std;

inline double max(double a, double b) { return a > b ? a : b; }
inline long long min(long long a, long long b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Or(int mask, int bit) { return mask | (1 << bit); }
inline int Xor(int mask, int bit) { return mask ^ (1 << bit); }

typedef pair<double, double> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
ii a[N];
int n, k;
double ans;
double getArea(double r) {
    return PI * r * r;
}
bool cmp(ii xx, ii yy) {
    return xx.ff > yy.ff;
    //double A = getArea(xx.ff) + 2 * PI * xx.ff * xx.ss;
    //double B = getArea(yy.ff) + 2 * PI * yy.ff * yy.ss;
    //return (A > B);
}

double solve(vector<ii> x) {
    double res = 0.0;
    double add, sub, onTop = 0.0;

    for (int i = x.size() - 1;i>=0;i--) {
        sub = getArea(x[i].ff) - onTop;
        add = 2.0 * PI * x[i].ff * x[i].ss;
        res += sub + add;
        onTop = getArea(x[i].ff);
    }
    return res;
}
int main() {
    #ifndef ONLINE_JUDGE
        freopen("exam.inp","r", stdin);
        freopen("exam.out","w", stdout);
    #endif
    int cases;
    scanf("%d", &cases);
    for (int it = 0;it < cases;it++) {
        scanf("%d %d", &n, &k);
        for (int i = 0;i < n;i++) {
            scanf("%lf %lf", &a[i].ff, &a[i].ss);
        }
        sort(a, a + n, cmp);
        ans = 0.0;
        /*vector <ii> cake;
        for (int i = 0;i < k;i++)
            cake.push_back(a[i]);
        ans = solve(cake);*/
        int limit = (1 << n);
        for (int i = 0;i < limit;i++) {
            int cnt = 0;
            vector<ii> cake;
            for (int j = 0;j < n;j++)
                if (And(i, j)) {
                    cake.push_back(a[j]);
                    cnt++;
                }
            if (cnt == k) {
                ans = max(ans, solve(cake));
            }
        }
        printf("Case #%d: %.9lf\n", it + 1, ans);
    }

    return 0;
}