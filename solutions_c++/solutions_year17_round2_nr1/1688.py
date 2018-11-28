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
const double eps = 1e-7;
const int maxn = 1e6 + 55;
const int maxk = 320;
const int base = 1e9 + 7;//1000200013;
const ll basell = 1e18 + 3;
const ld PI = acos(-1.0);

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

ld d, n;
ld k[maxn], s[maxn];

bool check(long double a){
    for(int i = 0; i < n; i++){
        if(k[i] + 1.0*s[i]*(d/a) < d)
            return 0;
    }
    return 1;
}

int main() {
    // srand(time(NULL));
    input;
      output;
    int t;
    cin >> t;
    int q = 1;
    while(q <= t){
        cin >> d >> n;
        ld time = 0;
        for(int i = 0; i < n; i++){
            cin >> k[i] >> s[i];
            time = max((d - k[i])/s[i], time);
        }
        cout << "Case #" << q << ": " << fixed << setprecision(10) << d/time << "\n";
        q++;
    }
    return 0;
}
