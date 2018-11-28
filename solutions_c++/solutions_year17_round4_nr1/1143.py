#include <bits/stdc++.h>
using namespace std;

#define int long long
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define ms(a, b) memset(a, b, sizeof(a))
#define optimize_io ios::sync_with_stdio(false); cin.tie(0)
#define ri(x) int x; cin >> x
#define rc(x) char x; cin >> x
#define r32(x) int32_t x; cin >> x
#define rll(x) long long x; cin >> x
#define rd(x) double x; cin >> x;
#define rld(x) long double x; cin >> x;

template<typename T> inline void read(T & x){ cin >> x; }
template<typename T, typename ... Types>
inline void read(T & x, Types & ...args){ cin >> x; }

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef long long ll;
typedef long double LD;

int dp[103][103][103][5];

int go(int a, int b, int c, int rem) {
    if(a+b+c == 0) return 0;
    int & res = dp[a][b][c][rem];
    if(res != -1) return res;
    res = 0;

    if(a > 0)
        res = max(res, go(a-1, b, c, (rem+1)%4));
    if(b > 0)
        res = max(res, go(a, b-1, c, (rem+2)%4));
    if(c > 0)
        res = max(res, go(a, b, c-1, (rem+3)%4));

    if(rem == 0) res++;
    return res;
}

void solve(int tn){ cout << "Case #" << tn << ": ";
    int n, p;
    cin >> n >> p;
    int freq[5] = {0};
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        freq[x%p]++;
    }

    int ans = 0;
    if(p == 2){
        ans += freq[0] + (freq[1]+1)/2;
    } else if(p == 3){
        ans += freq[0];
        int mx = max(freq[1], freq[2]);;
        int mn = min(freq[1], freq[2]);
        ans += mn;
        ans += (mx-mn+2)/3;
    } else {
        memset(dp, -1, sizeof dp);
        ans = freq[0] + go(freq[1], freq[2], freq[3], 0);
    }

    cout << ans << endl;
}

int32_t main(){
        int T;
    cin >> T;
    for(int i = 1; i <= T; i++)
        solve(i);
}
