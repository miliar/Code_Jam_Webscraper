#include <bits/stdc++.h>
const int MX=1555;
using namespace std;
typedef long double ld;
typedef long long ll;
bool M[MX],F[MX];
int dp[24*60+69][24*60+69][2][2];
/*
5
1 1
540 600
840 900
*/
int solve(int x,int rem,int Moth,int started)
{
    //assert(x>=0&&x<=24*60);
   // cout<<x<<endl;
    if(x==24*60)
    {
        if(rem==12*60)return started^Moth;
        return 1e4;
    }
    int& ret =dp[x][rem][Moth][started];
    if(ret!=-1)return ret;
      ret=24*60+6;
   if(x==0){
       if(M[x]^1)
        ret=min(ret,solve(x+1,rem+1,0,0));
    if(F[x]^1)
        ret=min(ret,solve(x+1,rem,1,1));
        return ret;
    }
    if(M[x]^1)
        ret=min(ret,solve(x+1,rem+1,0,started)+Moth);
    if(F[x]^1)
        ret=min(ret,solve(x+1,rem,1,started)+ !Moth);
    return ret;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("THESOeeeL.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int zbr=1;zbr<=t;zbr++)
    {
        int nm,nf;
        scanf("%d%d",&nm,&nf);
        memset(F,0,sizeof F);
        memset(M,0,sizeof F);
        for(int i=1;i<=nm;i++)
        {
            int l,r;
            scanf("%d%d",&l,&r);
            for(int j=l;j<r;j++)
                M[j]=1;
        }
        for(int i=1;i<=nf;i++)
        {
            int l,r;
            scanf("%d%d",&l,&r);
            for(int j=l;j<r;j++)
                F[j]=1;
        }
        memset(dp,-1,sizeof dp);
        printf("Case #%d: %d\n",zbr,min(solve(0,0,1,0),solve(0,0,0,1)));
        //cout<<<<endl;;

    }
}
