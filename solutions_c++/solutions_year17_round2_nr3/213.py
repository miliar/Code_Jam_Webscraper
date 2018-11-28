#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;
long long inf=1004567890000000000LL;

int main(){
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    long long tc;
    scanf("%lld",&tc);
    for(long long t=1;t<=tc;t++){
        long long n,q;
        scanf("%lld%lld",&n,&q);
        long long horsedis[n+10],speed[n+10];
        for(long long i=0;i<n;i++){
            scanf("%lld%lld",&horsedis[i],&speed[i]);
        }
        long long dis[n+10][n+10];
        long long a,b;
        for(long long i=0;i<n;i++){
            for(long long j=0;j<n;j++){
                scanf("%lld",&a);
                if(a==-1){
                    dis[i][j]=inf;
                }
                else{
                    dis[i][j]=a;
                }
            }
        }
        for(long long k=0;k<n;k++)
            for(long long i=0;i<n;i++)
                for(long long j=0;j<n;j++)
                    dis[i][j]=min(dis[i][k]+dis[k][j],dis[i][j]);

        //for(long long i=0;i<n;i++){for(long long j=0;j<n;j++)printf("%lld ",dis[i][j]);printf("\n");}

        double time[n+10][n+10];
        for(long long i=0;i<n;i++)
            for(long long j=0;j<n;j++)
                time[i][j]=inf;

        for(long long i=0;i<n;i++){
            for(long long j=0;j<n;j++){
                if(dis[i][j]<=horsedis[i]){
                    //printf("min %f %f\n",time[i][j],(double)dis[i][j]/speed[i]);
                    time[i][j]=min(time[i][j],(double)dis[i][j]/speed[i]);
                }
            }
        }

        for(long long k=0;k<n;k++)
            for(long long i=0;i<n;i++)
                for(long long j=0;j<n;j++)
                    time[i][j]=min(time[i][k]+time[k][j],time[i][j]);

        printf("Case #%lld: ",t);
        while(q--){
            scanf("%lld%lld",&a,&b);
            a--;b--;
            printf("%.6f ",time[a][b]);
        }
        printf("\n");
    }
    return 0;
}
