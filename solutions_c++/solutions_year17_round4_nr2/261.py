#include <bits/stdc++.h>

using namespace std;

#define fr first
#define sc second
#define pb push_back
#define ins insert
#define input freopen("input.txt","r",stdin)
#define output freopen("output.txt","w",stdout)
#define mp make_pair
#define fast_io ios_base::sync_with_stdio(0);
#define forn() for(int i=0;i<n;i++)
#define fori(n) for(ll i=0;i<(ll)n;i++)
#define forj(n) for(ll j=0;j<(ll)n;j++)
//iterator , unsigned, begin, end, count, continue
// fixed setprecision

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int inf = 2009000999;
const double eps = 1e-6;
const int maxn = 1e3 + 5;
const int maxk = 51;
const int base = 1000200013;
const ll basell = 1e18 + 3;
const ld PI = acos(-1.0);
const ll mod = 1e9 + 7;

string itosm(ll x){
    if(x == 0)
        return "0";
    string ans = "";
    while(x > 0){
        ans +=((x%10) + '0');
        x/=10;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

ll stoim(string str){
    ll ans = 0;
    ll k = 1;
    for(int i = str.length()-1; i >= 0; i--){
        ans+=(str[i]-'0')*k;
        k*=10;
    }
    return ans;
}

vector<int> a[1005];
int cnt[1005];

int main(){
    fast_io;
    input;
    output;
    int t;
    cin >> t;
    int q = 1;
    while(t--){
        int n, c, m;
        cin >> n >> c >> m;
        for(int i = 0; i < m; i++){
            int x, y;
            cin >> x >> y;
            cnt[x]++;
            a[y].pb(x);
        }
        //find ans1
        int ans1 = 0, ans2 = 0;
        for(int i = 0; i <= c; i++)
            ans1 = max(ans1,(int) a[i].size());
        int f = 0;
        for(int i = 1; i <= n; i++){
            ans1 = max(ans1, (f + cnt[i] + i - 1)/i);
            f += cnt[i];
        }
        if(n*ans1 < m){
            ans1 = (m + n - 1)/n;
            ans2 = 0;
        }

        //find ans2
        for(int i = 0; i <= n; i++){
            ans2 += max(0, cnt[i] - ans1);
        }

        cout << "Case #" << q << ": " << ans1 << " " << ans2 << "\n";
        for(int i = 0; i <= c; i++){
            a[i].clear();
        }
        for(int i = 0; i <= n; i++)
            cnt[i] = 0;
        q++;
    }
    return 0;
}
