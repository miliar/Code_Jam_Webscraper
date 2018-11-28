#include <bits/stdc++.h>
using namespace std;

#define loop(i,n) for(int i = 0;i < int(n);i++)
#define rloop(i,n) for(int i = int(n);i >= 0;i--)
#define range(i,a,b) for(int i = int(a);i <= int(b);i++)
#define SZ(c) int(c.size())
#define ALL(c) c.begin(), c.end()
#define RALL(c) c.rbegin(), c.rend()
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define sfi1(v) scanf("%d",&v)
#define sfi2(v1,v2) scanf("%d %d",&v1,&v2)
#define sfi3(v1,v2,v3) scanf("%d %d %d",&v1,&v2,&v3)
#define sfll1(v) scanf("%I64d",&v);
#define sfll2(v1,v2) scanf("%I64d %I64d",&v1,&v2)
#define sfll3(v1,v2,v3) scanf("%I64d %I64d %I64d",&v1,&v2,&v3)

typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long ll;
typedef pair<int, int> pii;

const double PI = acos(-1);
const int N = 1005;
double dp[N][N][3];
int r[N] , h[N];
pii p[N];
int n , k;

double solve(int idx = 0 , int l = 0 , int taken = 0){
    if(l == k || idx == n)return 0;
    double &ret = dp[idx][l][taken];
    if(ret == ret)return ret;
    ret = solve(idx+1 , l , taken);
    if(taken == 0)
        ret = max(ret , solve(idx+1, l+1 , 1) + PI * r[idx] * r[idx] + PI * 2 * r[idx] * h[idx]);
    else
        ret = max(ret , solve(idx+1, l+1 , taken) + PI * 2 * r[idx] * h[idx]);
    //cout << idx << ' ' << l << ' ' << taken << ' ' << ret << endl;
    return ret;
}


int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    int t;
    sfi1(t);
    range(T,1,t){
        sfi2(n,k);
        loop(i,n)sfi2(p[i].fr,p[i].sc);
        sort(p , p+n);
        reverse(p,p+n);
        loop(i,n)r[i] = p[i].fr , h[i] = p[i].sc;
        memset(dp,-1,sizeof dp);
        printf("Case #%d: %.9f\n",T,solve());
    }


    return 0;
}
