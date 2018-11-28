#include <stdio.h>
#include <algorithm>
#define N 100
using namespace std;

int n,p;
int num[N+5];
int cnt[5];
int dp3[N+5][N+5];
int dp4[N+5][N+5][N+5];
void solve (void)
{
    int i,ans=0;

    for(i=0;i<4;i++)
        cnt[i]=0;

    for(i=0;i<n;i++){
        num[i]%=p;
        cnt[num[i]]++;
    }

    if(p==2){
        ans += cnt[0];
        ans += (cnt[1]/2) + (cnt[1]%2);
    }
    else if(p==3){
        ans += cnt[0];
        ans += dp3[cnt[2]][cnt[1]];
    }
    else if(p==4){
        ans += cnt[0];
        ans += dp4[cnt[3]][cnt[2]][cnt[1]];
    }

    printf("%d\n",ans);

    return ;
}

void make_dp (void)
{
    int i,j,k;

    dp3[2][0]=dp3[1][0]=dp3[0][1]=dp3[0][2]=1;
    for(i=0;i<=N;i++){
        for(j=0;j<=N;j++){
            if(i>0 && j>0)
                dp3[i][j]=max(dp3[i][j],dp3[i-1][j-1]+1);
            if(j>2)
                dp3[i][j]=max(dp3[i][j],dp3[i][j-3]+1);
            if(i>2)
                dp3[i][j]=max(dp3[i][j],dp3[i-3][j]+1);
        }
    }

    dp4[1][0][0]=dp4[0][0][1]=dp4[0][1][0]=dp4[0][0][2]=dp4[0][0][3]=dp4[0][1][1]=dp4[2][0][0]=dp4[1][1][0]=dp4[3][0][0]=1;
    for(i=0;i<=N;i++){
        for(j=0;j<=N;j++){
            for(k=0;k<=N;k++){
                if(i>0 && k>0)
                    dp4[i][j][k]=max(dp4[i][j][k],dp4[i-1][j][k-1]+1);
                if(j>1)
                    dp4[i][j][k]=max(dp4[i][j][k],dp4[i][j-2][k]+1);
                if(j>0 && k>1)
                    dp4[i][j][k]=max(dp4[i][j][k],dp4[i][j-1][k-2]+1);
                if(k>3)
                    dp4[i][j][k]=max(dp4[i][j][k],dp4[i][j][k-4]+1);
                if(i>1 && j>0)
                    dp4[i][j][k]=max(dp4[i][j][k],dp4[i-2][j-1][k]+1);
                if(i>3)
                    dp4[i][j][k]=max(dp4[i][j][k],dp4[i-4][j][k]+1);
            }
        }
    }
}
int main (void)
{
    int i,j,T;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);

    make_dp();

    for(i=0;i<T;i++){
        scanf("%d %d",&n,&p);
        for(j=0;j<n;j++)
            scanf("%d",&num[j]);
        printf("Case #%d: ",i+1);
        solve();
    }


    return 0;
}
