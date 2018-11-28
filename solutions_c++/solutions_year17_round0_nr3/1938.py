#include<bits/stdc++.h>
#define PB(u)  push_back(u)
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 100005
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);
const int mod=1e9+7;

vector<ll> a;
void init()
{
    for(int i=0;  ;i++)
    {
        if((1ll<<i)>1e18) break;
        a.PB(1ll<<i);
    }
}


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    cin>>T;
    init();
    while(T--)
    {
        ll n,k;
        cin>>n>>k;
        printf("Case #%d: ",cas++);
        ll w= * (upper_bound(a.begin(),a.end(),k)-1);
        ll m=(n-k)/w;
        //cout<<w<<" "<<m<<endl;
        printf("%I64d %I64d\n",m-m/2,m/2);
    }
    return 0 ;
}

