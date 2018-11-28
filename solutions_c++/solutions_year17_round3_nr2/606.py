//#define WYTE 133
#include<bits/stdc++.h>
#define X first
#define Y second
#define mp(x,y) make_pair((x),(y))
#define eb(...) emplace_back(__VA_ARGS__)
#define SZ(x) int((x).size())
#define ALL(x) (x).begin(),(x).end()
#define INIT(x,y) memset((x),(y),sizeof(x))
#define arrayin(a,n) for(int _i=0;_i<n++_i){cin>>a[_i];}
#define arrayin1(a,n) for(int _i=1;_i<=n;++_i){cin>>a[_i];}
#define arrayout(a,n) for(int _i=0;_i<n;++_i){cout<<a[_i]<<" \n"[_i+1==n];}
#define arrayout1(a,n) for(int _i=1;_i<=n;++_i){cout<<a[_i]<<" \n"[_i+1>n];}
#define PQ priority_queue
#define IT iterator
#define INF 1e9
#define LLNF 1e18
#define EPS 1e-7
#define MOD 1000000007
#define MAX(a,b) a=max(a,b)
#define MIN(a,b) a=min(a,b)
#define mod(x) if(x>=MOD)x%=MOD
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int C[1500],J[1500],memo[750][750][2][2];
int dp(int c,int j,int prev,int start)
{
    if(c+j==720+720)return prev!=start;
    if(memo[c][j][prev][start]==-1)
    {
        memo[c][j][prev][start]=INF;
        if(!C[c+j]&&c+1<=720)
        {
            MIN(memo[c][j][prev][start],dp(c+1,j,0,start)+(prev!=0));
        }
        if(!J[c+j]&&j+1<=720)
        {
            MIN(memo[c][j][prev][start],dp(c,j+1,1,start)+(prev!=1));
        }
    }
    return memo[c][j][prev][start];
}
int main()
{
    freopen("B-large.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii,ac,aj,a,b,i,j;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        INIT(C,0);
        INIT(J,0);
        cin>>ac>>aj;
        for(i=0;i<ac;i++)
        {
            cin>>a>>b;
            for(j=a;j<b;j++)
            {
                C[j]=1;
            }
        }
        for(i=0;i<aj;i++)
        {
            cin>>a>>b;
            for(j=a;j<b;j++)
            {
                J[j]=1;
            }
        }
        INIT(memo,-1);
        printf("Case #%d: %d\n",ii,min(dp(0,0,0,0),dp(0,0,1,1)));
    }
}
