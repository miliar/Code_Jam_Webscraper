#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
using namespace std;

int main()
{
freopen("A-large (1).in","r",stdin);
freopen("A-large (1).out","w",stdout);
    int T;
    long long N,i,j,D;
    double S[100010];
    double K[100010];
    scanf("%d",&T);
    int ca=0;
    while(T--){
        ca++;
        cin>>D>>N;
        for (i=1;i<=N;i++)
            scanf("%lf%lf",&K[i],&S[i]);
        double ans=0;
        for (i=1;i<=N;i++)
            ans=max((D-K[i])/S[i]*1.0,ans);
           // cout<<ans<<endl;
        printf("Case #%d: %.6f\n",ca,D/ans);



    }



    return 0;
}
