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

int dp[721][721][2][2];
int day = 721;
bool usedc[1500];
bool usedj[1500];

void inline solve(){
    queue<pii> q;
    for(int i = 0; i < day; i++)
        for(int j = 0; j < day; j++)
            for(int g = 0; g < 2; g++)
                dp[i][j][0][g] = dp[i][j][1][g] = inf;
    dp[0][0][0][0] = dp[0][0][1][1] = 0;
    q.push(mp(0,0));
    while(!q.empty()){
        int x = q.front().fr, y = q.front().sc;
        q.pop();
//        cout << x << " " << y << " " << x + y << endl;
        if(usedc[x + y + 1] && x + 1 < day){
            bool update = 0;
            for(int j = 0; j < 2; j++)
                if(dp[x][y][0][j] < dp[x + 1][y][0][j]){
                    dp[x + 1][y][0][j] = dp[x][y][0][j];
                    update = 1;
                }
            for(int j = 0; j < 2; j++)
                if(dp[x][y][1][j] + 1 < dp[x + 1][y][0][j]){
                    dp[x + 1][y][0][j] = dp[x][y][1][j] + 1;
                    update = 1;
                }
            if(update)
                q.push(mp(x + 1, y));
        }
        if(usedj[x + y + 1] && y + 1 < day){
            bool update = 0;
            for(int j = 0; j < 2; j++)
                if(dp[x][y][1][j] < dp[x][y + 1][1][j]){
                    dp[x][y + 1][1][j] = dp[x][y][1][j];
                    update = 1;
                }
            for(int j = 0; j < 2; j++)
                if(dp[x][y][0][j] + 1 < dp[x][y + 1][1][j]){
                    dp[x][y + 1][1][j] = dp[x][y][0][j] + 1;
                    update = 1;
                }
            if(update)
                q.push(mp(x, y + 1));
        }
    }
}

int main(){
    input;
//    output;
    ofstream fout("output.txt");
    fast_io;
    int taskCase;
    cin >> taskCase;
    int taskCaseCnt = 1;
    while(taskCaseCnt <= taskCase){
        int ac, aj;
        cin >> ac >> aj;
        for(int i = 0; i < 2*day; i++)
            usedc[i] = usedj[i] = 1;
        for(int i = 0; i < ac; i++){
            int l, r;
            cin >> l >> r;
            for(int j = l + 1; j <= r; j++)
                usedc[j] = 0;
        }
        for(int i = 0; i < aj; i++){
            int l, r;
            cin >> l >> r;
            for(int j = l + 1; j <= r; j++)
                usedj[j] = 0;
        }
        solve();
        cout << taskCaseCnt << endl;
        fout << "Case #" << taskCaseCnt << ": "  << min(min(dp[720][720][0][1] + 1, dp[720][720][1][0] + 1),
                                                       min(dp[720][720][0][0], dp[720][720][1][1])) << "\n";
        taskCaseCnt++;
    }
    return 0;
}
