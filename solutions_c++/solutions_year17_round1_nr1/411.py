#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

#define pb push_back
#define mp make_pair
#define f first
#define s second

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) FOR(i, 0, a)

const int MAX = 200005;
const int MOD = 1000000007;
const int MAGIC = 3;

char ar[30][30];

int n, m;
bool ok(int i, int j) {
    return (0<=i && i<n && 0<=j && j<m && ar[i][j] == '?');
}
bool check(int a, int b, int c, int d) {
    for (int i=a; i<=c; i++) {
        for (int j=b; j<=d; j++) {
            if (!ok(i, j)) { return false; }
        }
    }
    return true;
}
void exp(int i, int j) {
    int a=i, b=j, c=i, d=j;
    F0R(i, 50) {
        if (check(a-1, b, a-1, d)) { a--; }
        if (check(a, d+1, c, d+1)) { d++; }
        if (check(c+1, b, c+1, d)) { c++; }
        if (check(a, b-1, c, b-1)) { b--; }
    }
    for (int t=a; t<=c; t++) {
        for (int u=b; u<=d; u++) {
            ar[t][u] = ar[i][j];
        }
    }
}
int main() {
    int tc; cin >> tc;
    freopen("lol.txt", "w", stdout);
    F0R(t, tc) {
        cout << "Case #" << t+1 << ":" << endl;
        cin >> n >> m;
        F0R(i, n) {
            F0R(j, m) {
                cin >> ar[i][j];
            }
        }
        vector<pii> v;
        F0R(i, n) { F0R(j, m) { if (ar[i][j] != '?') { v.pb({i, j}); } } }
        for (pii i : v) { exp(i.f, i.s); }
        F0R(i, n) { F0R(j, m) { cout << ar[i][j]; } cout << endl; }
    }
}
