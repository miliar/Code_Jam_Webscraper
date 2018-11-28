#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef double db;
const db PI=acos(-1.0);
ll R[1005],H[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)
            scanf("%lld%lld",&R[i],&H[i]);
        db res=0;
        for(int i=1;i<=n;i++)
        {
            vector<ll>tmp;
            for(int j=1;j<=n;j++)
                if(i!=j && R[j]<=R[i])
                    tmp.push_back(R[j]*H[j]);
            if((int)tmp.size()<k-1)continue;
            sort(tmp.begin(),tmp.end(),greater<ll>());
            ll sum=R[i]*R[i]+2*R[i]*H[i];
            for(int i=0;i<k-1;i++)
                sum+=2*tmp[i];
            res=max(res,sum*PI);
        }
        printf("Case #%d: %.12f\n",ca,res);
    }
    return 0;
}
