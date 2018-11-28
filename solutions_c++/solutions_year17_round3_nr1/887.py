#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.txt", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
typedef long long LL;
typedef pair<int,int> pii;
const int MOD = 1e9 + 7;
const int MAX = 1e5 + 5;
const double PI = 3.141592653589793;
int n, k;
vector<pair<double, double> > v;
int memo[1001][1001];
double dp[1001][1001];

double solve(int cur, int cnt){
    if(cnt == k) return 0;
    if(cur == n) return -1e18;
    if(memo[cur][cnt]) return dp[cur][cnt];
    memo[cur][cnt] = 1;

    double ans = solve(cur+1, cnt);
    if(cnt == 0){
        ans = max(ans, solve(cur+1, cnt+1) + PI*v[cur].F*v[cur].F + 2*PI*v[cur].F*v[cur].S);
    }
    else{
        ans = max(ans, solve(cur+1, cnt+1) + 2*PI*v[cur].F*v[cur].S);
    }
    return dp[cur][cnt] = ans;
}

int main() {
    fr;fw;
    cout << fixed << setprecision(9);
    int T, cases = 1;
    cin >> T;
    while(T--){
        v.clear();
        cin >> n >> k;
        REP(i, n){
            int r, h;
            cin >> r >> h;
            v.pb(mp(r, h));
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        cout <<"Case #" << cases++<<": ";
        CLEAR(memo);
        cout << solve(0, 0) <<"\n";
    }
    return 0;
}