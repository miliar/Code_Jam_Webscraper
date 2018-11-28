#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<pair<int,int>,pair<int,int>>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
#define MOD 1000000007
#define LD long double
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(;c<'0'||c>'9';c=getchar())if(c=='-')sign=-1;
    for(num=0;c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

int A[1003][2],sel[1003];
int done[1003][1003];
vector<int> V[1003],W[1003];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests;
    tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        int n=getnum(),c=getnum(),m=getnum(),ans;

        for(int i=1;i<=1000;i++)
        {
            V[i].clear();
            W[i].clear();
            for(int j=0;j<=1000;j++)done[i][j]=0;
        }

        for(int i=1;i<=m;i++)
        {
            A[i][0]=getnum();
            A[i][1]=getnum();

            V[A[i][0]].pb(A[i][1]);
        }
        ans=m;

        for(int i=1;i<=m;i++)
        {
            for(int j=1;j<=1000;j++)sel[j]=0;

            int rem=0,flag=0;
            for(int j=1;j<=1000;j++)
            {
                rem++;
                for(int k=0;k<V[j].size()&&rem;k++)
                {
                    if(sel[V[j][k]]==0&&done[j][k]==0)
                    {
                        flag=1;
                        sel[V[j][k]]=1;
                        rem--;
                        done[j][k]=1;
                    }
                }
            }
            if(flag==0)
            {
                ans=i-1;
                break;
            }
        }

        for(int i=1;i<=1000;i++)
        {
            for(int j=0;j<=1000;j++)done[i][j]=0;
        }

        for(int i=1;i<=1000;i++)
        {
            for(int j=0;j<V[i].size();j++)
            {
                W[V[i][j]].pb(i);
            }
        }

        int tot=0;

        for(int i=1;i<=1000;i++)
        {
            for(int j=0;j<W[i].size();j++)
            {
                int flag=0;
                for(int k=1;k<=ans;k++)
                {
                    if(done[k][W[i][j]]==0){done[k][W[i][j]]=1,flag=1;break;}
                }
                if(flag==0)tot++;
            }
        }

        printf("Case #%d: %d %d\n",cases,ans,tot);
    }
}
