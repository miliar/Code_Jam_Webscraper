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

int A[5];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests;
    tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        int n=getnum(),p=getnum();

        for(int i=0;i<p;i++)A[i]=0;

        for(int i=1;i<=n;i++)
        {
            int x=getnum();
            A[x%p]++;
        }

        if(p==2)
        {
            printf("Case #%d: %d\n",cases,A[0]+(A[1]+1)/2);
        }
        if(p==3)
        {
            int mn=min(A[1],A[2]);
            int mx=max(A[1],A[2]);
            printf("Case #%d: %d\n",cases,A[0]+mn+(mx-mn+2)/3);
        }
    }
}
