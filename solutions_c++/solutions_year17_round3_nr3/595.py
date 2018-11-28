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
    freopen("C-small-1-attempt1.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii,n,k,u,i;
    long double tmp,p[50],ans;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>n>>k>>tmp;
        u=tmp*100000;
        for(i=0;i<n;i++)
        {
            cin>>p[i];
        }
        while(u)
        {
            sort(p,p+n);
            p[0]+=0.00001;
            u--;
        }
        ans=1;
        for(i=0;i<n;i++)
        {
            ans*=p[i];
        }
        printf("Case #%d: %Lf\n",ii,ans);
    }
}
