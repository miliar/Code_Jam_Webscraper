#include <bits/stdc++.h>
using namespace std;
#define input freopen("C:\\cp\\A-large.in","r",stdin)
#define output freopen("C:\\cp\\out.txt","w",stdout)
#define sz(x) ((int)(x).size())
#define all(x) ((x).begin(), (x).end())
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define double long double
const double PI = acos(-1.0);
typedef pair<int,int> pii;
typedef long long ll;

const double oo = 1e18;
const int MAX = 1005;

struct cake{
    double R,H;
    bool operator<(const cake& o) const{
        return R > o.R;
    }
}C[MAX];

int n,k;
double dp[MAX][MAX][2];
bool vis[MAX][MAX][2];

double solve(int i,int f, int rem)
{
    if(i >= n){
        if(rem == 0) return 0;
        return -oo;
    }
    if(rem == 0) return 0;
    if(vis[i][rem][f])
        return dp[i][rem][f];
    vis[i][rem][f] = 1;
    double r = solve(i+1, f, rem);
    if(f){
        r = max(r, PI * C[i].R * C[i].R + 2 * PI * C[i].R * C[i].H + solve(i+1, 0, rem-1));
    }else{
        r = max(r, 2 * PI * C[i].R * C[i].H + solve(i+1, 0, rem-1));
    }
    return dp[i][rem][f] = r;
}

int main()
{
	input;
	output;
	int T,tc(1);
	cin >> T;
	while(T--){
        cin >> n >> k;
        for(int i=0;i<n;i++){
            cin >> C[i].R >> C[i].H;
        }
        sort(C,C+n);
        memset(vis,0,sizeof vis);
        double ans = solve(0,1,k);
        cout << fixed << setprecision(8) << "Case #" << tc++ << ": " << ans << endl;
	}
    return 0;
}








