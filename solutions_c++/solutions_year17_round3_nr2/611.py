#include <bits/stdc++.h>
using namespace std;

#define loop(i,n) for(int i = 0;i < int(n);i++)
#define rloop(i,n) for(int i = int(n);i >= 0;i--)
#define range(i,a,b) for(int i = int(a);i <= int(b);i++)
#define SZ(c) int(c.size())
#define ALL(c) c.begin(), c.end()
#define RALL(c) c.rbegin(), c.rend()
#define PI acos(-1)
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

const int N = 1502;
const int M = 725;
int notfree[2][N];
int c , j , s , e;
int dp[N][M][3][3];

//we mara p = 1
int solve(int idx = 0 , int u = 0 , int p = 0 , int s = 0){
    if(idx == 1440){
        if(u == 720)return s != p;
        return N + N;
    }
    int &ret = dp[idx][u][p][s];
    if(~ret)return ret;
    if(notfree[p][idx])return ret = N+N;
    return ret = min(solve(idx+1 , u + (p == 0) , 0 , s) + (p==1)
                     ,solve(idx+1 , u + (p == 0) , 1 , s) + (p==0));

}

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    int t;
    sfi1(t);
    range(T,1,t){
        memset(notfree,0,sizeof notfree);
        memset(dp,-1,sizeof dp);
        sfi2(c,j);
        loop(i,c){
            sfi2(s,e);
            range(k,s,e-1)
                notfree[0][k] = 1;
        }

        loop(i,j){
            sfi2(s,e);
            range(k,s,e-1)
                notfree[1][k] = 1;
        }

        printf("Case #%d: %d\n",T,min(solve(0,0,0,0) , solve(0,0,1,1)));
    }



    return 0;
}
