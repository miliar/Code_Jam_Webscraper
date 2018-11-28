#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pair<int,int> >
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
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

ll pow10[20],A[20];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    pow10[0]=1;

    for(int i=1;i<=18;i++)pow10[i]=pow10[i-1]*10;

    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        ll r=getnum();
        ll l=1,ans=-1;
        int done=0;

        for(int i=18;i>=0;i--)
        {
            A[i]=(r/pow10[i])%10;

            if(A[i]<A[i+1])
            {
                while(i>=0)
                {
                    A[i]=A[i+1];
                    i--;
                }
                break;
            }
        }

        ll rr=0;
        for(int i=0;i<=18;i++)rr+=pow10[i]*A[i];

        if(rr==r)done=1,ans=r;

        while(l<r&&!done)
        {
            ll m=(l+r)/2;

            for(int i=18;i>=0;i--)
            {
                A[i]=(m/pow10[i])%10;

                if(A[i]<A[i+1])
                {
                    while(i>=0)
                    {
                        A[i]=A[i+1];
                        i--;
                    }
                    break;
                }
            }

            ll mm=0;
            for(int i=0;i<=18;i++)mm+=pow10[i]*A[i];

            if(mm>r)r=m;
            else if(mm<=r)l=mm+1,ans=mm;
        }

        printf("Case #%d: %lld\n",cases,ans);
    }
}
