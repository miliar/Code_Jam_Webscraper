#include <bits/stdc++.h>

using namespace std;
#define int int64_t
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define endl '\n'

template<typename T>
void sci(T& t) {
    cin >> t;
}

template<typename T, typename... Ts>
void sci(T& t, Ts&... ts) {
    sci(t);
    sci(ts...);
}

#define scid(vars...) int vars; sci(vars)
#ifndef HOME
#define FASTIO cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
#define debug(...)
#define __DEBUG if (0) {
#define DEBUG__ }
#define cerr if (0) cerr
#else //HOME
#define FASTIO
#define debug(...) printf("$"); printf(__VA_ARGS__)
#define __DEBUG
#define DEBUG__
#endif // HOME

#define YN(ans) cout << ((ans) ? "YES" : "NO") << endl

#define forn(i,n)    for (int (i) = 0; (i)<(int)(n); ++(i))
#define forkn(i,k,n) for (int (i) = (int)(k); (i)<(int)(n); ++(i))
#define forit(i,container)    for (auto (i) : container)
#define itout(container)    cout << "\n$"; for (auto _it : container) cout << _it << ' ';

typedef long double ld;
typedef long long ll;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pld;

typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<ll> vll;
typedef vector<pll> vpll;
typedef vector<ld> vld;
typedef vector<pld> vpld;

typedef vector<vi> graph;
typedef vector<vpii> wgraph;

#define MAXN 500010
#define inf 2000000000
#define INFLL 2000000000000000000LL
#define MOD 1000000007
#define HASHMOD 793877113
#define SQRT 320
#define PI 3.141592653589

int32_t main(){
    //freopen("out.txt", "w", stdout);
    scid(T);
    string s;
    getline(cin, s);
    forn(time, T){
        getline(cin, s);
        int i = 0;
        vi kek;
        while(!(s[i] >= '0' && s[i] <= '9')){
            if(s[i] == ' '){
                i++;
                continue;
            }
            kek.pb((s[i] == '+' ? 1 : 0));
            i++;
        }
        int k = 0;
        int ans = 0;
        while(i < s.length()){
            k *= 10;
            k += s[i] - '0';
            i++;
        }
        int n = kek.size();
        forn(i, n - k + 1){
            if(kek[i] == 1){
                continue;
            }
            ans++;
            forn(j, k){
                kek[i+j] = 1 - kek[i+j];
            }
        }
        bool check = 1;
        forn(i, n){
            check &= (kek[i] == 1);
        }
        cout << "Case #" << time + 1 << ": ";
        if(!check){
            cout << "IMPOSSIBLE\n";
        }
        else{
            cout << ans << endl;
        }
    }
    return 0;
}
