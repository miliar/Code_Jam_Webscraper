#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 
#define ON 0
#define DEBUG(x) if (ON) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

inline bool DEQ(double a, double b) { return fabs(a-b) < 1e-9; }
// const int INF = 1<<29;

const double PI = 3.14159265;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef pair<int, int> pii;
#define pb push_back
#define mp make_pair

inline int shl(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

double circle(int r) {
    return PI * r * r;
}
double keliling(int r, int h) {
    return 2 * PI * r * h;
}
double luas(int r, int h, int prev_rad) {
    return circle(r) - circle(prev_rad) + keliling(r, h);
}

double choose(vector<pii>& pancake, vector<vector<double> >& memo, int n, int k, int prev_rad, vii& take) {
    DEBUG(n);
    DEBUG(k);
    if (n - k < 0 || n < 0 || k < 0) {
        return 0;
    }
    
    if (memo[n][k] >= 0) {
        return memo[n][k];
    }
    
    double check1 = choose(pancake, memo, n-1, k, prev_rad, take);
    double check2 = choose(pancake, memo, n-1, k-1, pancake[n-1].first, take) + luas(pancake[n].first, pancake[n].second, prev_rad);
    memo[n][k] = max(memo[n][k], check1);
    memo[n][k] = max(memo[n][k], check2);
    if (check1 > check2) {
        DEBUG(check1);
        DEBUG(n);
        DEBUG(k);
        DEBUG(pancake[n].first);
    } else {
        DEBUG(check2);
        DEBUG(n);
        DEBUG(k);
        DEBUG(pancake[n].first);
    }
    DEBUG(memo[n][k]);

    return memo[n][k];
}

void execute() {
    int N, K;
    scanf("%d %d", &N, &K);
    vector<pii> pancake(N);
    vector<vector<double> > memo(N, vector<double>(K, -1));
    REP(i, N) {
        // R H
        scanf("%d %d", &pancake[i].first, &pancake[i].second);
    }
    sort(pancake.begin(), pancake.end());
    // double area = 0;
    // int prev_rad = 0;
    // FORD(i, K - 1, 0) {
    //     area += circle(pancake[i].first) - circle(prev_rad);
    //     area += keliling(pancake[i].first, pancake[i].second);
    //     prev_rad = pancake[i].first;
    // }
    vii take;
    N--;
    K--;
    choose(pancake, memo, N, K, 0, take);
    printf("%.9lf\n", memo[N][K]);
}

int main() {
    int tc = 0;
    scanf("%d", &tc);
    FOR(i, 1, tc) {
        printf("Case #%d: ", i);
        execute();
    }
}
