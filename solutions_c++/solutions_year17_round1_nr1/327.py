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

string a[MAXN];

bool check(int x, int y, int X, int Y, char c) {
    bool ok = 1;
    for(int i = x; i <= X; i++)
        for(int j = y; j <= Y; j++) {
            ok &= (a[i][j] == '?' || a[i][j] == c);
            if(!ok) {
                // cout << i << " " << j << "\n";
            }
        }
    return ok;
}

int main() {
    freopen(".in", "r", stdin);
    freopen("t.out", "w", stdout);

    int test; cin >> test;
    for(int num = 1; num <= test; num++) {
        cout << "Case #" << num << ":\n"; 
    
        int n, m; cin >> n >> m;

        vector<int> us(26, 0);
        for(int i = 0; i < n; i++) {
            cin >> a[i];
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++)
                if(a[i][j] != '?' && !us[a[i][j] - 'A']) {
                    us[a[i][j] - 'A'] = 1;

                    int x = i;
                    int y = j;
                    int X = i;
                    int Y = j;

                    while(y > 0 && check(x, y - 1, X, Y, a[i][j]))
                        y--;
                    while(Y != m - 1 && check(x, y, X, Y + 1, a[i][j]))
                        Y++;
                    while(x > 0 && check(x - 1, y, X, Y, a[i][j]))
                        x--;
                    while(X != n - 1 && check(x, y, X + 1, Y, a[i][j]))
                        X++;

                    for(int q = x; q <= X; q++)
                        for(int w = y; w <= Y; w++)
                            a[q][w] = a[i][j];
                }
        }

        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++) {
                if(a[i][j] == '?') {
                    cerr << num << "\n";
                    return 0;
                }
            }

        for(int i = 0; i < n; i++)
            cout << a[i] << "\n";
    }
}
