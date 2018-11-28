// In the name of god
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <bitset>
#define sqr(a) ((a)*(a))
#define all(a) (a).begin(), (a).end()
using namespace std;
 
template <typename T>
T next_int() {
    T x = 0, p = 1;
    char ch;
    do { ch = getchar(); } while(ch <= ' ');
    if(ch == '-') {
        p = -1;
        ch = getchar();
    }
    while(ch >= '0' && ch <= '9') {
        x = x * 10 + (ch - '0');
        ch = getchar();
    }
    return p * x;
}
 
string next_token() {
    char ch;
    string ans = "";
    do { ch = getchar(); } while(ch <= ' ');
    while(ch > ' ') {
        ans += ch;
        ch = getchar();
    }
    return ans;
}
 
const long long INF = (long long)1e18;
const int INFINT = (int)1e9 + 227 + 1;
const int MAXN = (int)1e6 + 227 + 1;    
const int MOD = (int)1e9 + 7;
const long double EPS = 1e-9;

long long bin_pow(long long a, long long b) {
    if(!b) return 1;
    long long ans = bin_pow(a, b / 2);
    ans = ans * ans % MOD;
    if(b % 2) ans = ans * a % MOD;
    return ans;
}

bool us[MAXN];
int l[MAXN];
int r[MAXN];

pair<int, int> brut(int n, int m) {
    for(int i = 0; i < n; i++)
        us[i] = 0;

    pair<int, int> last = make_pair(-1, -1);
    for(int it = 0; it < m; it++) {
        for(int i = 0; i < n; i++) {
            if(us[i])
                l[i] = -1;
            else
                l[i] = (i ? l[i - 1] + 1 : 0);
        }
        for(int i = n - 1; i >= 0; i--) {
            if(us[i])
                r[i] = -1;
            else
                r[i] = (i + 1 < n ? r[i + 1] + 1 : 0);
        }

        pair<int, int> kek = make_pair(-1, -1); 
        int p = -1;
        for(int i = 0; i < n; i++) {
            pair<int, int> temp = make_pair(min(l[i], r[i]), max(l[i], r[i]));

            if(temp > kek) {
                kek = temp;
                p = i;
            }
        }

        us[p] = 1;
        last = kek;
    }

    swap(last.first, last.second);
    return last;
}

int main() {
    freopen(".in", "r", stdin);
    freopen("ans.out", "w", stdout);

    int test; cin >> test;

    for(int number_test = 1; number_test <= test; number_test++) {
        cout << "Case #" << number_test << ": ";

        int n, m; cin >> n >> m;

        pair<int, int> ans = brut(n, m);

        cout << ans.first << " " << ans.second << "\n";

        // return 0;
    }
}
