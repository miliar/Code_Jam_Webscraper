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
const double eps = 1e-3;
const int maxn = 2e5 + 55;
const int maxk = 55;
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

ofstream fout("output.txt");
map<ll, ll> s;

void solve(ll &n, ll &k, int &q){
    ll ans1, ans2;
//    s.max_load_factor(0.25);
    s.clear();
    s[-n] = 1;
    while(k > 0){
        pair<ll, ll> a = (*s.begin());
        s.erase(s.begin());
        a.fr = -a.fr;
        if(a.fr & 1){
            if(a.fr > 1){
                s[(-(a.fr>>1))] += a.sc*2;
            }
            k -= a.sc;
            ans1 = a.fr/2;
            ans2 = ans1;
        }
        else{
            if(a.fr > 1){
                s[(-(a.fr>>1))] += a.sc;
            }
            if(a.fr > 3){
                s[(-((a.fr>>1) - 1))] += a.sc;
            }
            ans1 = a.fr>>1;
            ans2 = ans1 - 1;
            k -= a.sc;
        }
//        cout << ans1 << " " << ans2 << "\n";
    }
//    while(k--){
//        int a = -(*s.begin());
//        s.erase(s.begin());
//        if(a & 1){
//            if(a > 1){
//                s.insert(-(a>>1));
//                s.insert(-(a>>1));
//            }
//            ans1 = a/2;
//            ans2 = ans1;
//        }
//        else{
//            if(a > 1)
//                s.insert(-(a>>1));
//            if(a > 3)
//                s.insert(-((a>>1) - 1));
//            ans1 = a>>1;
//            ans2 = ans1 - 1;
//        }
//        cout << ans1 << " " << ans2 << "\n";
//    }
    fout << "Case #" << q << ": ";
    fout << ans1 << " " << ans2 << "\n";
}

int main() {
//    srand(time(NULL));
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("output_file.txt", "w", stdout);
    input;
//    output;
    fast_io;
    int t = 100000;
    cin >> t;
    int q = 1;
    while(q <= t){
        cout << q << " - " << 1.0*clock()/CLOCKS_PER_SEC << "\n";
        ll n, k;
//        n = 1LL*rand()*rand()*rand()*rand() + 4, k = 1LL*rand()*rand()*rand()*rand() % n;
        cin >> n >> k;
        solve(n, k, q);
        q++;
    }
	return 0;
}
