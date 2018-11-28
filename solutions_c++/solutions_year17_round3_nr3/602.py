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

double p[1000];

int main(){
    input;
    output;
    fast_io;
    int taskCase, taskCaseCnt = 1;
    cin >> taskCase;
    while(taskCaseCnt <= taskCase){
        int n, k;
        cin >> n >> k;
        double u;
        cin >> u;
        for(int i = 0; i < n; i++)
            cin >> p[i];
        sort(p, p + n);
        while(u > 0){
            int j = -1;
            for(int i = 1; i < n; i++)
                if(p[i] != p[0]){
                    j = i;
                    break;
                }
            if(j != -1){
                if(u/j > p[j] - p[0]){
                    u -= (p[j] - p[0])*(j);
                    for(int i = 0; i < j; i++)
                        p[i] = p[j];
                }
                else{
                    for(int i = 0; i < j; i++)
                        p[i] += u/j;
                    u = 0;
                }
            }
            else{
                for(int i = 0; i < n; i++){
                    p[i] += (u/n);
                    p[i] = min(1.0, p[i]);
                }
                u = 0;
            }
        }
        ld ans = 1;
        for(int i = 0; i < n; i++)
            ans *= p[i];
        cout << "Case #" << taskCaseCnt << ": "  << fixed << setprecision(20) << ans << "\n";
        taskCaseCnt++;
    }
    return 0;
}
