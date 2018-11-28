#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int n,q;

double inf=1e13;

int speed[105],limit[105];

int G[105][105];

double dp[105][105];

double ldist[105][105];

void prep1(){
    for(int i=1;i<n;i++){
        for(int j=i+1;j<=n;j++){
            ldist[i][j]=ldist[i][j-1]+G[j-1][j];
        }
    }
}

double call(int index, int horse){
    if (limit[horse]<ldist[horse][index]){
        dp[index][horse]=inf;
        return inf;
    }

    if (dp[index][horse]!=-1){
        return dp[index][horse];
    }
    if (index==n){
        return 0;
    }


    double ret1,ret2;

    ret1=(double)G[index][index+1]/(double)speed[index];

    ret1+=call(index+1,index);

    ret2=(double)G[index][index+1]/(double)speed[horse];

    ret2+=call(index+1,horse);

    dp[index][horse]=min(ret1,ret2);

    return dp[index][horse];


}


int main(){
    freopen("C-small-attempt0.in","r",stdin); freopen("C-small-1.txt","w",stdout);

    int t;
    cin>>t;

    for(int tc=1;tc<=t;tc++){

        for(int i=0;i<=102;i++){
            for(int j=0;j<=102;j++){
                dp[i][j]=-1;
                ldist[i][j]=0;
            }
        }

        //memset(ldist,0,sizeof(ldist));

        /*for(int i=0;i<=10;i++){
            cout<<dp[i][7]<<ldist[i][6]<<endl;
        }*/


        cin>>n>>q;

        for(int i=1;i<=n;i++){
            cin>>limit[i];
            cin>>speed[i];
        }

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                cin>>G[i][j];
            }
        }
        prep1();
        int u,v;

        printf("Case #%d: ",tc);

        for(int i=0;i<q;i++){
            cin>>u>>v;

            double ans=call(1,1);
            printf("%.7f\n",ans);

        }



    }


}

