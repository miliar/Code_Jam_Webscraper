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

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,d,n,k[1005],s[1005],ii,i;
    double slowest;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>d>>n;
        slowest=0;
        for(i=0;i<n;i++)
        {
            cin>>k[i]>>s[i];
            slowest=max(slowest,(double)(d-k[i])/s[i]);
        }
        printf("Case #%d: %lf\n",ii,d/slowest);
    }
}
