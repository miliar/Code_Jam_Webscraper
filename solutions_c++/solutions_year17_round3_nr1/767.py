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
const int maxn = 1e6 + 55;
const int maxk = 55;
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

pair<ld, ld> a[1005];
pair<ld, int> b[1005];
int n, k;

ld brut(){
    ll ans = 0, ans1;
    for(int i = 0; i < 1 << n; i++){

    }
}

bool comp(pair<ld, int> c, pair<ld, int> d){
    if(c.fr * a[c.sc].fr > d.fr * a[d.sc].fr)
        return 0;
    return 1;
}

int main(){
    input;
    output;
    fast_io;
    int taskCase;
    cin >> taskCase;
    int taskCaseCnt = 1;
    while(taskCaseCnt <= taskCase){
        cin >> n >> k;
        for(int i = 0; i < n; i++){
            cin >> a[i].fr >> a[i].sc;
            b[i].sc = a[i].fr;
            b[i].fr = a[i].sc;
        }
        ld ans = 0, ans1 = 0;
        sort(a, a + n);
        reverse(a, a + n);
        for(int i = 0; i < n; i++){
            b[i].sc = i;
            b[i].fr = a[i].sc;
        }
        sort(b, b + n, comp);
        reverse(b, b + n);
        for(int t = 0; t <= n - k; t++){
            ans1 = a[t].fr * a[t].fr * PI + a[t].fr * a[t].sc * 2 * PI;
            int cnt = 1;
            for(int i = 0; i < n && cnt < k; i++){
                if(a[b[i].sc].fr <= a[t].fr && b[i].sc != t){
                    cnt++;
                    ans1 += 2 * PI * a[b[i].sc].fr * b[i].fr;
                }
            }
            if(cnt == k)
                ans = max(ans, ans1);
        }
        cout << "Case #" << taskCaseCnt << ": "  << fixed << setprecision(20) << ans << "\n";
        taskCaseCnt++;
    }
    return 0;
}
