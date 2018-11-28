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

int cnt[5];

int main(){
    fast_io;
    input;
    output;
    int t;
    cin >> t;
    int q = 1;
    while(t--){
        int n, p;
        cin >> n >> p;
        int ans = 0;
        for(int i = 0; i < n; i++){
            int a;
            cin >> a;
            cnt[a % p]++;
        }
        ans = cnt[0];
        if(p == 2){
            ans += (cnt[1] + 1)/2;
        }
        else if(p == 3){
            ans += min(cnt[1], cnt[2]);
            int f = min(cnt[1], cnt[2]);
            cnt[1] -= f;
            cnt[2] -= f;
            ans += (cnt[1] + 2)/3;
            ans += (cnt[2] + 2)/3;
        }
        else{
            ans += cnt[2]/2;
            cnt[2] %= 2;
            int f = min(cnt[1], cnt[3]);;
            ans += f;
            cnt[1] -= f;
            cnt[3] -= f;
            ans += (cnt[1] + 3)/4;
            ans += (cnt[3] + 3)/4;
            if((cnt[1] + cnt[3])%4 == 0)
                ans += cnt[2];
        }
        for(int i = 0; i < 5; i++)
            cnt[i] = 0;
        cout << "Case #" << q << ": " << ans << "\n";
        q++;
    }
    return 0;
}
