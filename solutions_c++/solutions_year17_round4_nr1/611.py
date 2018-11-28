#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

#define Rep(i,n) for(int i=0;i<(n);++i)
#define Repd(i,n) for(int i=((int)(n))-1;i>=0;--i)
#define For(i,a,b) for(int i=(a);i<=(b);++i)
#define Ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fi first
#define se second
#define pb push_back
#define MP make_pair

typedef pair<int,int> PII;
typedef vector<int> VI;

#define debug cout << "Here " << __LINE__ << endl;
template <typename T> ostream& operator<<(ostream &os, vector<T> v) { Rep(i, v.size()) os << v[i] << " "; os << endl; return os; }
template <typename T1, typename T2> ostream& operator<<(ostream &os, pair<T1, T2> p) { os << "(" << p.fi << ", " << p.se << ")"; return os; }

int n, p;
int a[101];
int c[4];
int F[101][101][101][101];
// int C[101][101][101];

int solve(int p0, int p1, int p2, int p3) {
    if (p0 + p1 + p2 + p3 == 0) {
        return 0;
    }
    int &res = F[p0][p1][p2][p3];
    if (res != -1) return res;
    res = 0;
    int c[] = {p0, p1, p2, p3};
    int total = 0;
    Rep(i, p) total += c[i] * i;
    Rep(i, p) if (c[i] > 0) {
        --c[i];
        int lastTotal = (total - i);
        int good = lastTotal % p == 0 ? 1 : 0;
        res = max(res, good + solve(c[0], c[1], c[2], c[3]));
        ++c[i];
    }
    return res;
}

int main() {
    int nt;
    cin >> nt;
    Rep(t, nt) {
        cin >> n >> p;
        Rep(i, n) cin >> a[i];
        memset(c, 0, sizeof(c));
        Rep(i, n) c[a[i] % p]++;
        memset(F, -1, sizeof(F));
        int res = solve(c[0], c[1], c[2], c[3]);
        cout << "Case #" << (t + 1) << ": " << res << endl;
    }
    return 0;
}
