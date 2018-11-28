#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define si(a)           scanf("%d",&a)
#define sii(a,b)        scanf("%d %d",&a,&b)
#define siii(a,b,c)     scanf("%d %d %d",&a,&b,&c)

#define sl(a)           scanf("%I64d",&a)
#define sll(a,b)        scanf("%I64d %I64d",&a,&b)
#define slll(a,b,c)     scanf("%I64d %I64d %I64d",&a,&b,&c)

#define pb              push_back
#define PII             pair <int,int>
#define PLL             pair <ll,ll>
#define mp              make_pair
#define xx              first
#define yy              second
#define all(v)          v.begin(),v.end()

#define CLR(a)          memset(a,0,sizeof(a))
#define SET(a)          memset(a,-1,sizeof(a))

#define eps             1e-9
#define PI              acos(-1.0)
#define MAX             105
#define MOD             1000000007
#define INF             2000000000000000000

int setBit(int n,int pos){ return n = n | (1 << pos); } //sets the pos'th bit to 1
int resetBit(int n,int pos){ return n = n & ~(1 << pos); } //sets the pos'th bit to 0
bool checkBit(int n,int pos){ return (bool)(n & (1 << pos)); } //returns the pos'th bit

/******************************************************************************************/

ld E[MAX],S[MAX],D[MAX][MAX],CD[MAX];
bool vis[MAX][MAX];
ld dp[MAX][MAX];
int N;

ld call(int pos,int last)
{
    if(pos==N) return 0;
    if(vis[pos][last]) return dp[pos][last];
    int x = pos+1;
    ld y , ret = INF;
    if(last==0){
        y = call(2,1);
        y += (CD[2]-CD[1])/S[1];
        ret = min(ret,y);
    }
    else{
        if(CD[x]-CD[last]<=E[last]){
            y = call(x,last);
            y += (CD[x]-CD[pos])/S[last];
            ret = min(ret,y);
        }

        if(CD[x]-CD[pos]<=E[pos]){
            y = call(x,x-1);
            y += (CD[x]-CD[pos])/S[pos];
            ret = min(ret,y);
        }
    }
    vis[pos][last] = true;
    return dp[pos][last] = ret;
}



int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.txt","w",stdout);

    int t,T,Q,i,j,p,q;
    si(T);
    for(t=1;t<=T;t++){
        CLR(vis);
        sii(N,Q);



        for(i=1;i<=N;i++) cin >> E[i] >> S[i];

        for(i=1;i<=N;i++){
            for(j=1;j<=N;j++) cin >> D[i][j];
        }
        for(i=1;i<=Q;i++) cin >> p >> q;
        CD[1] = 0;
        for(i=2;i<=N;i++) CD[i] = CD[i-1] + D[i-1][i];

        ld ans = call(1,0);

        cout << setprecision(10) << fixed << "Case #" << t << ": " << ans << endl;


    }


    return 0;
}

