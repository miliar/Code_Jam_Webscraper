#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
#define fi first
#define se second
using namespace std;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
int main()
{
    freopen("txtin.txt","r",stdin);
    freopen("txtout.txt","w",stdout);
    int t,n,i,j,k,l,m,r1,r2;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cout<<"Case #"<<test<<":\n";
        cin>>n>>m;
        int sum[30]={0};
        bool vis[30]={0};
        char ch[30][30];
        //pair<int,int> ans[30][30];
        for(i=1;i<=n;i++)
        {

            for(j=1;j<=m;j++){
                cin>>ch[i][j];
                //ans[i][j]=mp(i,j);
                if(ch[i][j]!='?')
                 {
                     sum[i]++;
                 }
            }
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(ch[i][j]!='?'){
                for(k=i-1;k>0;k--)
                {
                    if(ch[k][j]!='?')
                        break;
                    ch[k][j]=ch[i][j];
                }
                for(k=i+1;k<=n;k++)
                {
                    if(ch[k][j]!='?')
                        break;
                    ch[k][j]=ch[i][j];
                }
                }
            }
        }


        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(ch[i][j]!='?')
                {
                    for(k=j-1;k>0;k--)
                {
                    if(ch[i][k]!='?')
                        break;
                    ch[i][k]=ch[i][j];
                }
                for(k=j+1;k<=m;k++)
                {
                    if(ch[i][k]!='?')
                        break;
                    ch[i][k]=ch[i][j];
                }
                }
            }
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
                cout<<ch[i][j];
            cout<<"\n";
        }
    }
    return 0;
}
