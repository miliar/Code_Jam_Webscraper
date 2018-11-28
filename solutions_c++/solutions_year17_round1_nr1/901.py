//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

int ar[100][100];
string dd,L,R;

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    int i,j,k,l,n,cas,test,flag,temp,now,ans=0,m;
    char ch;
    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        memset(ar,0,sizeof(ar));
        cin>>n>>m;

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                cin>>ch;
                ar[i][j]=ch;
            }
        }

        for(i=1;i<=n;i++)
        {
            flag=0;
            for(j=1;j<=m;j++) if(ar[i][j]!='?') flag=1;
            if(flag)
            {
                for(j=1;j<=m;j++)
                {
                    now=-1;
                    for(k=j;k<=m;k++)
                    {
                        if(ar[i][k]!='?')
                        {
                            now=ar[i][k];
                            break;
                        }
                    }

                    if(now!=-1) ar[i][j]=now;

                    if(now==-1)
                    {
                        for(k=j;k>=1;k--)
                        {
                            //if(i==1 && j==2) cout<<ar[i][k]<<" ";
                            if(ar[i][k]!='?')
                            {
                                now=ar[i][k];
                                break;
                            }
                        }
                        ar[i][j]=now;
                    }

                    //if(now==-1) cout<<i<<"  mm  "<<j<<endl;
                }
            }
            else
            {
                for(j=1;j<=m;j++) ar[i][j]=ar[i-1][j];
            }
        }

        for(i=n;i>=1;i--)
        {
            for(j=1;j<=m;j++)
            {
                if(ar[i][j]>'Z' || ar[i][j]<'A') ar[i][j]=ar[i+1][j];
            }
        }

        printf("Case #%d:\n",cas);
        //cout<<n<<" "<<m<<endl;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                cout<<(char)(ar[i][j]);
            }
            cout<<endl;
        }

    }



}
