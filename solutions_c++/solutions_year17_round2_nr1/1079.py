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

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        double t=0;
        int d,n;
        scanf("%d%d",&d,&n);
        for(int i=1;i<=n;i++)
        {
            int k,s;
            scanf("%d%d",&k,&s);
            t=max(t,1.0*(d-k)/s);
        }
        printf("Case #%d: %.10f\n",cas++,d/t);
    }
    return 0 ;
}

