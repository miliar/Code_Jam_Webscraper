#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <ctime>

#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<ld, ld> point;

const int N = (int)(1e5) + 7;
const int M = (int)(32);
const ld eps = 1e-12;
const ll MOD = (ll)(1e9) + 7;
const ll INF = (ll)(1e9) + 7;

void solve(int ttt) {
    printf("Case #%d: ", ttt);
    string s;
    int n;
    cin >> s >> n;
    int cnt = 0;
    for (int i = 0; i <= (int)(s.size()) - n; ++i) {
        if (s[i] == '-') {
            for (int j = i; j < i + n; ++j)
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            ++cnt;
        }
    }
    int f = 0;
    for (int i = 0; i < (int)(s.size()); ++i)
        if (s[i] == '-')
            f = 1;
    if (f)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << cnt << endl;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    //freopen("sum.in", "r", stdin);
    //freopen("sum.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
    return 0;
}
