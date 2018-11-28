// hloya template v24
  
// ░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░░░░░
// ░░░░░░█░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░█░░░░░
// ░░░░░░█░█░▀░░░░░▀░░▀░░░░█░█░░░░░
// ░░░░░░█░█░░░░░░░░▄▀▀▄░▀░█░█▄▀▀▄░
// █▀▀█▄░█░█░░▀░░░░░█░░░▀▄▄█▄▀░░░█░
// ▀▄▄░▀██░█▄░▀░░░▄▄▀░░░░░░░░░░░░▀▄
// ░░▀█▄▄█░█░░░░▄░░█░░░▄█░░░▄░▄█░░█
// ░░░░░▀█░▀▄▀░░░░░█░██░▄░░▄░░▄░███
// ░░░░░▄█▄░░▀▀▀▀▀▀▀▀▄░░▀▀▀▀▀▀▀░▄▀░
// ░░░░█░░▄█▀█▀▀█▀▀▀▀▀▀█▀▀█▀█▀▀█░░░
// ░░░░▀▀▀▀░░▀▀▀░░░░░░░░▀▀▀░░▀▀░░░░
  
#include <bits/stdc++.h>
#include <valarray>
using namespace std;
  
bool dbg = 0;
  
clock_t start_time = clock();
#define current_time fixed<<setprecision(6)<<(ld)(clock()-start_time)/CLOCKS_PER_SEC
  
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
  
#define ll long long
#define ld long double
#define pii pair<int,int>
#define umap unordered_map<int, int>
  
#define files1 freopen("input.txt","r",stdin)
#define files2 freopen("out2.txt","w",stdout)
#define files files1;files2
#define fast_io ios_base::sync_with_stdio(0);cin.tie(0)
  
#define endl '\n'
#define ln(i,n) " \n"[(i) == (n) - 1]
  
void bad(string mes = "Impossible"){cout << mes;exit(0);}
void bad(int mes){cout << mes;exit(0);}
  
template<typename T>
string bin(T x, int st = 2){
    string ans = "";
    while (x > 0){
        ans += char('0' + x % st);
        x /= st;
    }
    reverse(ans.begin(), ans.end());
    return ans.empty() ? "0" : ans;
}
  
template<typename T>
void amax(T& x, T y) {
    x = max(x, y);
}
  
template<typename T>
void amin(T& x, T y) {
    x = min(x, y);
}
  
template<typename T>
T input(){
    T ans = 0, m = 1;
    char c = ' ';
  
    while (!((c >= '0' && c <= '9') || c == '-')) {
        c = getchar();
    }
  
    if (c == '-')
        m = -1, c = getchar();
    while (c >= '0' && c <= '9'){
        ans = ans * 10 + (c - '0'), c = getchar();
    }
    return ans * m;
}
  
template<typename T> void read(T& a) { a = input<T>(); }
template<typename T> void read(T& a, T& b) { read(a), read(b); }
template<typename T> void read(T& a, T& b, T& c) { read(a, b), read(c); }
template<typename T> void read(T& a, T& b, T& c, T& d) { read(a, b), read(c, d); }
  
const int inf = 2e9 + 20;
const short short_inf = 3e4 + 20;
const long double eps = 1e-12;
const int maxn = 1e5 + 12, base = 1e9 + 7;
const ll llinf = 2e18 + 5;
  
template<typename T>
T binpow(T n, T s)
{
    if (s <= 0)
        return 1LL;
    if (s % 2 == 0){
        T b = binpow(n, s / 2);
        return ( 1LL * b * b ) % base;
    } else {
        return (1LL* binpow(n, s - 1) * n) % base;
    }
}

ll dp[20][10][2];
int R[20], sz;

void parse(ll x) {
    sz = 0;
    while (x) {
        R[sz++] = x % 10;
        x /= 10;
    }
    reverse(R, R + sz);
}

void solve(int t) {
    printf("Case #%d: ", t);
    ll n;
    cin >> n;

    if (n < 10) {
        printf("%lld\n", n);
        return;
    }

    memset(dp, 0, sizeof(dp));
    parse(n);

    ll ans1 = 0;
    for (int i = 0; i < sz - 1; i++)
        ans1 = ans1 * 10ll + 9;

    for (int i = 1; i < R[0]; i++)
        dp[0][i][0] = i;
    dp[0][R[0]][1] = R[0];

    for (int i = 0; i + 1 < sz; i++) {
        for (int last = 0; last < 10; last++) 
            for (int ndig = last; ndig < 10; ndig++) {
                if (dp[i][last][0])
                    amax(dp[i + 1][ndig][0], dp[i][last][0] * 10ll + ndig);
                if (dp[i][last][1]) {
                    if (ndig < R[i + 1])
                        amax(dp[i + 1][ndig][0], dp[i][last][1] * 10ll + ndig);
                    if (ndig == R[i + 1])
                        amax(dp[i + 1][ndig][1], dp[i][last][1] * 10ll + ndig);
                }
            }
    }
    for (int l = 0; l < 10; l++)
        amax(ans1, max(dp[sz - 1][l][1], dp[sz - 1][l][0]));
    printf("%lld\n", ans1);
}

int main() {
    files;
    int t;
    fast_io;
    cin >> t;

    for (int i = 1; i <= t; i++)
        solve(i);
    return 0;
}