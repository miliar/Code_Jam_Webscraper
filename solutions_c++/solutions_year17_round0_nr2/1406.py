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

int main() {
//    srand(time(NULL));
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("output_file.txt", "w", stdout);
    input;
    output;
    fast_io;
    int t = 100;
    cin >> t;
    int q = 1;
    while(q <= t){
        string s;
        cin >> s;
        int n = s.length();
        for(int f = 0; f < 20; f++)
            for(int i = 0; i + 1 < n; i++){
                if(s[i] > s[i + 1]){
                    s[i]--;
                    for(int j = i + 1; j < n; j++)
                        s[j] = '9';
                }
            }
        cout << "Case #" << q << ": ";
        if(s[0] == '0')
            for(int i = 1; i < n; i++)
                cout << s[i];
        else
            cout << s;
        cout << "\n";
        q++;
    }
	return 0;
}
