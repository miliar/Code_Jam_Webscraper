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

int p;
map<vi,int> memo[4];
int dp(int left,vi &cnt)
{
    int i,ans=0,chk=0;
    for(i=0;i<p;i++)
    {
        if(cnt[i])chk=1;
    }
    if(chk==0)return 0;
    if(memo[left].find(cnt)==memo[left].end())
    {
        for(i=0;i<p;i++)
        {
            if(cnt[i]==0)continue;
            cnt[i]--;
            MAX(ans,dp((left+i)%p,cnt));
            cnt[i]++;
        }
        memo[left][cnt]=ans+(left==0);
    }
    return memo[left][cnt];
}

int main()
{
    freopen("A-large.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii,n,i,g;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>n>>p;
        vi cnt(p);
        for(i=0;i<p;i++)
        {
            memo[i].clear();
        }
        for(i=0;i<n;i++)
        {
            cin>>g;
            cnt[g%p]++;
        }
        printf("Case #%d: %d\n",ii,dp(0,cnt));
    }
}
