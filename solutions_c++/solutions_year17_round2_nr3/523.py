#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define F first
#define S second
#define pp pair<int,int>
using namespace std;
int n,Q;
ll E[105],S[105];
ll D[105][105];
double timer[105][105];


int main(){
    freopen("C-large.in","r",stdin); freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        cin>>n>>Q;
        for(int i=0;i<n;i++)cin>>E[i]>>S[i];

        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                cin>>D[i][j];
                if(D[i][j]==-1)
                    D[i][j]=1000000000000000000ll;
            }

        for(int k=0;k<n;k++)
            for(int i=0;i<n;i++)
                for(int j=0;j<n;j++)
                    D[i][j]=min(D[i][j],D[i][k]+D[k][j]);

        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(E[i]>=D[i][j])
                    timer[i][j]=D[i][j]/(double)S[i];
                else
                    timer[i][j]=1000000000000000000.0;
        /*for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
                cout<<timer[i][j]<<' ';
            cout<<endl;
        }*/
        for(int k=0;k<n;k++)
            for(int i=0;i<n;i++)
                for(int j=0;j<n;j++)
                    timer[i][j]=min(timer[i][j],timer[i][k]+timer[k][j]);
        cout<<"Case #"<<t<<":";
        while(Q--){
            int u,v;
            cin>>u>>v;
            u--;v--;
            printf(" %.9lf",timer[u][v]);
        }
        cout<<endl;

    }
    return 0;
}
