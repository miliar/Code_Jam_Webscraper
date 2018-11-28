//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

string aa;
long long ar[100009];
vector<long long>vec,ANS;
long long dp[25][15][5];
long long KEEP[25][15][5];
long long SIZ,vis[25][15][5];

long long GO(long long curr,long long past,long long flag)
{
    if(curr==SIZ) return 1;
    if(vis[curr][past][flag]) return dp[curr][past][flag];
    vis[curr][past][flag]=1;

    long long i;

    //cout<<curr<<" "<<past<<" "<<flag<<endl;

    if(flag)
    {
        KEEP[curr][past][flag]=9;
        return dp[curr][past][flag]=GO(curr+1,9,flag);
    }
    else
    {
        for(i=vec[curr];i>=past;i--)
        {
            if(GO(curr+1,i,i<vec[curr]))
            {
                KEEP[curr][past][flag]=i;
                return dp[curr][past][flag]=1;
            }
        }

        return dp[curr][past][flag]=0;
    }
}

void PRNT(long long curr,long long past,long long flag)
{
    if(curr==SIZ) return;
    ANS.push_back(KEEP[curr][past][flag]);
    long long flagg=flag;
    if(flag==0) if(KEEP[curr][past][flag]<vec[curr]) flagg=1;
    PRNT(curr+1,KEEP[curr][past][flag],flagg);
}

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    long long i,j,k,l,n,cas,test,flag,temp,now,ans=0,siz;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n;
        vec.clear();
        ANS.clear();
        while(n)
        {
            vec.push_back(n%10);
            n/=10;
        }

        reverse(vec.begin(),vec.end());
        siz=vec.size();
        SIZ=siz;
        memset(vis,0,sizeof(vis));

        GO(0,0,0);
        PRNT(0,0,0);

        printf("Case #%lld: ",cas);
        flag=0;
        for(i=0;i<ANS.size();i++)
        {
            if(ANS[i]) flag=1;
            if(flag) cout<<ANS[i];
        }
            cout<<endl;

    }



}
