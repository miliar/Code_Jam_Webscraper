#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
lli power(int x,int y)
{
    if(y==0)
        return 1;

    if(y&1)
        return x*power(x,y-1);
    lli ans= power(x,y/2);
    return ans*ans;
}

int t,cas,r,c;
string str[30];
int main()
{
    int i,j,k,cnt;
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        cas++;
        scanf("%d %d",&r,&c);
        for(i=0; i<r; i++)
            cin>>str[i];

        for(i=0; i<r; i++)
        {
            cnt=0;
            for(j=0; j<c; j++)
            {
                if(str[i][j]=='?')
                {
                    if(j-1>=0 && str[i][j-1]!='?')
                        str[i][j]=str[i][j-1];
                    else if(j+1<c && str[i][j+1]!='?')
                    {
                        for(k=j; k>=0 && str[i][k]=='?'; k--)
                            str[i][k]=str[i][j+1];
                        cnt=0;
                    }
                    else
                        cnt++;
                }
            }
            if(cnt==c)
            {
                for(j=0; j<c; j++)
                {
                    if(i>0 && str[i-1][j]!='?')
                        str[i][j]=str[i-1][j];
                }
            }

            if(i-1>=0)
            {
                for(j=0; j<c; j++)
                {
                    if(str[i-1][j]=='?')
                        str[i-1][j]=str[i][j];
                }
            }
        }

        for(i=r-1;i>=0;i--){
                cnt=0;
            for(j=0;j<c;j++){
                if(str[i][j]=='?')
                    cnt++;
            }
            if(cnt==c){
                if(i+1<r){
                    for(j=0;j<c;j++)
                        str[i][j]=str[i+1][j];
                }
            }
        }

        printf("Case #%d:\n",cas);
        for(i=0; i<r; i++)
            cout<<str[i]<<"\n";
    }
    return 0;
}
