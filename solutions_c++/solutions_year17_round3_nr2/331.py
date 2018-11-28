#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pii>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
#define MOD 1000000007LL
#define ld long double
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(; c<'0'||c>'9'; c=getchar())if(c=='-')sign=-1;
    for(num=0; c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

int A[4000];
int dp[1500][730][3][3];

int func(int cur,int tot,int st,int prev)
{
    if(tot>720)return 10000;
    if(cur-tot>720)return 10000;

    int &ans=dp[cur][tot][st][prev];
    if(ans!=-1)return ans;

    if(cur==1440)
    {
        if(prev!=st)return ans=1;
        else return ans=0;
    }

    if(A[cur]==1)
    {
        int x=func(cur+1,tot+1,st,1);
        if(prev==1)return ans=x;
        if(prev==2)return ans=1+x;
    }

    if(A[cur]==2)
    {
        int x=func(cur+1,tot,st,2);
        if(prev==2)return ans=x;
        if(prev==1)return ans=1+x;
    }

    if(A[cur]==0)
    {
        int x=func(cur+1,tot+1,st,1);
        int y=func(cur+1,tot,st,2);

        ans=10000;

        if(prev==1)ans=min(ans,x);
        else ans=min(ans,1+x);

        if(prev==2)ans=min(ans,y);
        else ans=min(ans,1+y);
    }

    //cout<<cur<<' '<<tot<<' '<<st<<' '<<prev<<' '<<ans<<endl;

    return ans;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        for(int i=0;i<1500;i++)
            for(int j=0;j<730;j++)
                for(int k=1;k<=2;k++)
                    for(int l=1;l<=2;l++)dp[i][j][k][l]=-1;

        int a=getnum(),b=getnum();
        int n=a+b;

        for(int i=0;i<=1440;i++)A[i]=0;

        for(int i=1;i<=a;i++)
        {
            int x=getnum(),y=getnum();
            for(int j=x;j<y;j++)A[j]=1;
        }

        for(int i=1;i<=b;i++)
        {
            int x=getnum(),y=getnum();
            for(int j=x;j<y;j++)A[j]=2;
        }

        int ans;

        if(A[0]!=0)
        {
            if(A[0]==1)ans=func(1,1,1,1);
            else if(A[0]==2)ans=func(1,0,2,2);
        }
        else
        {
            ans=min(func(1,1,1,1),func(1,0,2,2));
        }

        printf("Case #%d: %d\n",cases,ans);
        cerr<<"Case #"<<cases<<endl;
    }
}
