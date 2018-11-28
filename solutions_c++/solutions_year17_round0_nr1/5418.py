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
const int MAXN = (int)1e3 + 227 + 1;    
const int MOD = (int)1e9 + 7;
const long double EPS = 1e-9;

long long bin_pow(long long a, long long b) {
    if(!b) return 1;
    long long ans = bin_pow(a, b / 2);
    ans = ans * ans % MOD;
    if(b % 2) ans = ans * a % MOD;
    return ans;
}

int main() {
    freopen(".in", "r", stdin);
    freopen("ans.out", "w", stdout);

    int test; cin >> test;

    for(int number_test = 1; number_test <= test; number_test++) {
        cout << "Case #" << number_test << ": ";

        string a = next_token();
        int k = next_int<int>();

        int ans = 0;
        for(int i = 0; i + k <= a.size(); i++) {
            if(a[i] == '-') {
                for(int j = i; j < i + k; j++)
                    a[j] = (a[j] == '+' ? '-' : '+');
                ans++;
            }
        }

        bool ok = 1;
        for(int i = 0; i < a.size(); i++)
            ok &= (a[i] == '+');
        
        if(!ok)
            cout << "IMPOSSIBLE";
        else
            cout << ans;
        puts("");
    }
}
