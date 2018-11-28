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
  
const int inf = 1e9 + 20;
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

int hd, ad, hk, ak, b, d, shd;

bool turn(char t) {
    if (t == 'a' && ad >= hk) {
        hk -= ad;
        return 1;
    }

    int op_att = ak;
    if (t == 'd') {
        op_att -= d;
    }

    if (op_att >= hd) {
        hd = shd;
        hd -= ak;
        return false;
    }

    if (t == 'd') {
        ak = max(0, ak - d);
    }
    if (t == 'b') {
        ad = ad + b;
    }
    if (t == 'a') {
        hk -= ad;
    }

    assert(hd > ak);
    hd -= ak;
    return 1;
}

void solve(int t) {
    printf("Case #%d: ", t);

    int sad, shk, sak, sb, sd;
    cin >> shd >> sad >> shk >> sak >> sb >> sd;

    int ans = inf;
    for (int cntMovesd = 0; cntMovesd <= 100; cntMovesd++)
        for (int cntMovesb = 0; cntMovesb <= 100; cntMovesb++) {
    // int cntMovesb = 0, cntMovesd = 0;
            int cur = 0;
            hd = shd, ad = sad, hk = shk, ak = sak, b = sb, d = sd;

            int wr = 0;
            for (int i = 0; i < cntMovesd && wr < cntMovesd + 5;) {
                if(turn('d'))
                    i++;
                else
                    wr++;
                if (hd < 0)
                    cur = inf;
                cur++;
            }
            // cout << wr;
            if (wr == cntMovesd + 5)
                continue;

            wr = 0;
            for (int i = 0; i < cntMovesb && wr < cntMovesb + 5;) {
                if(turn('b'))
                    i++;
                else
                    wr++;
                if (hd < 0)
                    cur = inf;
                cur++;
            }
            if (wr == cntMovesb + 5)
                continue;
            // cout << cur << endl;
            // exit(0);

            wr = 0;
            while (hk > 0 && wr < 105) {
                if (turn('a') == false)
                    wr++;
                // cout << hd << ' ' << hk << endl;
                if (hd < 0)
                    cur = inf;
                cur++;
            }
            // cout << wr;
            if (wr == 105)
                continue;

            // cout << cntMovesb << ' ' << cntMovesd;
            // exit(0);

            amin(ans, cur);
        }

    if (ans == inf)
        puts("IMPOSSIBLE");
    else
        printf("%d\n", ans);
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