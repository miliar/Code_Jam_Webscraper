// hloya template v25
  
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

inline int popcount(int x){
    int count = 0;
    __asm__ volatile("POPCNT %1, %0;":"=r"(count):"r"(x):);
    return count;
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
const int maxn = (int)1e6 + 2e5 + 12, base = 1e9 + 7;
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

int need[51];
int have[51][51];

vector<int> enters[51][maxn];
multiset<int> lines[51];

void solve(int t) {
    printf("Case #%d:", t);
    cerr << t << endl;
    int n, p;
    cin >> n >> p;

    for (int i = 0; i < n; i++) {
        cin >> need[i];
        lines[i].clear();
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < maxn; j++)
            enters[i][j].clear();

    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++) {
            cin >> have[i][j];
            int l = (have[i][j] * 10 + 11 * need[i] - 1) / (11 * need[i]);
            int r = (have[i][j] * 10) / (9 * need[i]);
            
            // cout << l << ' ' << r << endl;
            if (l <= r) {
                assert(l >= 1 && l < maxn);
                assert(r >= 1 && r < maxn);

                enters[i][l].pb(r);
            }
        }
    int ans = 0;
    for (int i = 1; i < maxn; i++) {
        for (int j = 0; j < n; j++) {
            while (!lines[j].empty() && (*lines[j].begin()) < i)
                lines[j].erase(lines[j].begin());
            for (int k : enters[j][i])
                lines[j].insert(k);
        }
        while (1) {
            bool ok = 1;
            for (int j = 0; j < n; j++)
                if (lines[j].empty())
                    ok = 0;
            if (!ok)
                break;
            ans++;
            for (int j = 0; j < n; j++)
                lines[j].erase(lines[j].begin());
        }
    }
    printf(" %d\n", ans);
}

int main() {
    files;
    fast_io;
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
        solve(i);
    return 0;
}