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

int main()
{
    freopen("B-large.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii,i,j;
    ll n;
    char num[20];
    cin>>t;
    for(ii=1;ii<=t;++ii)
    {
        cin>>n;
        sprintf(num,"%lld",n);
        for(i=strlen(num)-1;i>0;--i)
        {
            if(num[i-1]>num[i])
            {
                --num[i-1];
                for(j=i;num[j];++j)
                {
                    num[j]='9';
                }
            }
        }
        sscanf(num,"%lld",&n);
        cout<<"Case #"<<ii<<": "<<n<<"\n";
    }
}
