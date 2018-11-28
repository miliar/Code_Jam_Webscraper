#define WYTE 133
#include<bits/stdc++.h>
#define X first
#define Y second
#define mp(x,y) make_pair((x),(y))
#define eb(...) emplace_back(__VA_ARGS__)
#define SZ(x) int((x).size())
#define ALL(x) (x).begin(),(x).end()
#define INIT(x,y) memset((x),(y),sizeof(x))
#define PQ priority_queue
#define IT iterator
#define INF 1e9
#define EPS 1e-7
#define MOD 1000000007
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

pii solve(int n,int k)
{
    if(k==1)
    {
        return mp((n-1)/2,n/2);
    }
    else
    {
        --k;
        if(k%2)
        {
            return solve(n/2,k/2+1);
        }
        else
        {
            return solve((n-1)/2,k/2);
        }
    }
}
int main()
{
    freopen("C-small-2-attempt0.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii;
    ll n,k;
    cin>>t;
    for(ii=1;ii<=t;++ii)
    {
        cin>>n>>k;
        pii p=solve(n,k);
        cout<<"Case #"<<ii<<": "<<max(p.X,p.Y)<<' '<<min(p.X,p.Y)<<"\n";
    }
}
