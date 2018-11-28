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

int main() {
    // srand(time(NULL));
    input;
    output;
    int t;
    cin >> t;
    int q = 1;
    while(q <= t){
        int n;
        cin >> n;
        int r, o, y, g, b, v;
        cin >> r >> o >> y >> g >> b >> v;
        // r + y = o
        // y + b = g
        // r + b = v
        string ans = "";
        while(n > 0){
            bool make = 0;
            if(r > y && r > b){
                if(ans[0] != 'R'){
                    r--;
                    ans = 'R' + ans;
                    make = 1;
                }
                else if(ans[ans.length() - 1] != 'R'){
                    r--;
                    ans += 'R';
                    make = 1;
                }
            }
            else if(y > r && y > b){
                if(ans[0] != 'Y'){
                    y--;
                    ans = 'Y' + ans;
                    make = 1;
                }
                else if(ans[ans.length() - 1] != 'Y'){
                    y--;
                    ans += 'Y';
                    make = 1;
                }
            }
            else if(b > 0){
                if(ans[0] != 'B'){
                    b--;
                    ans = 'B' + ans;
                    make = 1;
                }
                else if(ans[ans.length() - 1] != 'B'){
                    ans += 'B';
                    make = 1;
                    b--;
                }
            }
            if(!make){
                if(r > 0 &&!make && ans[0] != 'R'){
                    ans = 'R' + ans;
                    make = 1;
                    r--;
                }
                else if(r > 0 && !make && ans[ans.length() - 1] != 'R'){
                    ans += 'R';
                    make = 1;
                    r--;
                }
                if(y > 0 && !make && ans[0] != 'Y'){
                    ans = 'Y' + ans;
                    make = 1;
                    y--;
                }
                else if(y > 0 && !make && ans[ans.length() - 1] != 'Y'){
                    ans += 'Y';
                    y--;
                    make = 1;
                }
                if(b > 0 && !make && ans[0] != 'B'){
                    ans = 'B' + ans;
                    b--;
                    make = 1;
                }
                else if(b > 0 && !make && ans[ans.length() - 1] != 'B'){
                    ans += 'B';
                    b--;
                    make = 1;
                }
            }
            if(!make)
                break;
            n--;
        }
        if(n > 0)
            ans = "IMPOSSIBLE";
        else if(ans[0] == ans[ans.length() - 1]){
            for(int i = 2; i < ans.length() - 1; i++){
                if(ans[i - 1] != ans[0] && ans[i] != ans[i - 2]){
                    swap(ans[0], ans[i - 1]);
                    break;
                }
            }
            if(ans[0] == ans[ans.length() - 1])
                ans = "IMPOSSIBLE";
        }
        cout << "Case #" << q << ": " << ans << "\n";
        q++;
    }
    return 0;
}
