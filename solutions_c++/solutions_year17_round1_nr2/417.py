#include <bits/stdc++.h>
using namespace std;

#define int long long
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

const int MAX = 55;
const int MOD = 1000000007;
const int MAGIC = 3;

template <typename T>
std::ostream& operator<< (std::ostream& out, const std::vector<T>& v) {
  if ( !v.empty() ) {
    out << '[';
    std::copy (v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}

int need[MAX];
vector<int> ing[MAX];
int lb[MAX];
int ub[MAX];
int n, m;
int moo(int serv) {
    int ans = 0;
    F0R(i, n) {
        lb[i] = ceil(need[i]*serv*.9);
        ub[i] = floor(need[i]*serv*1.1);
        while (!ing[i].empty() && ing[i].back() < lb[i]) { ing[i].pop_back(); }
    }
    while (1) {
        int ct = 0;
        F0R(i, n) {
            if (!ing[i].empty() && ing[i].back() <= ub[i]) { ct++; }
        }
        if (ct == n) {
            ans++;
            F0R(i, n) { ing[i].pop_back(); }
        }
        else { return ans; }
    }
}

main() {
    freopen("B-large.in", "r", stdin);
    int tcs; cin >> tcs;
    F0R(t, tcs) {
        F0R(i, 50) { ing[i].clear(); }
        cin >> n >> m;
        F0R(i, n) { cin >> need[i]; }
        F0R(i, n) {
            F0R(j, m) { int a; cin >> a; ing[i].pb(a); }
            sort(ing[i].begin(), ing[i].end());
            reverse(ing[i].begin(), ing[i].end());
        }
        int fin = 0;
        FOR(i, 1, 1000001) { fin += moo(i); }
        cout << "Case #" << t+1 << ": " << fin << endl;
    }
}
/*
2 8
10 20
11 13 17 11 16 14 12 18
22 26 34 22 32 28 24 36
*/
