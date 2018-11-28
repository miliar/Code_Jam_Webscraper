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
    cin >> s;
    if (s.size() == 1) {
        cout << s << endl;
        return ;
    }
    for (int i = 0; i < (int)(s.size()) - 1; ++i) {
        if (s[i] > s[i + 1]) {
            while (i && s[i] == s[i - 1])
                --i;
            s[i]--;
            for (int j = i + 1; j < (int)(s.size()); ++j)
                s[j] = '9';
            int j = i;
            while (j && s[j] == '0') {
                s[j] = '9';
                if (j)
                    s[j - 1]--;
                --j;
            }
        }
    }
    if (s[0] == '0')
        cout << s.substr(1, s.size() - 1) << endl;
    else
        cout << s << endl;
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
