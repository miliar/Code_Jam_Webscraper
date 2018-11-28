#include<bits/stdc++.h>
#define ll long long
#define pii pair<double,int>
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

pii R[1003];
double A[1003],H[1003];

const double pi = 3.141592653589793238L;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        int n=getnum(),k=getnum();

        for(int i=1;i<=n;i++)
        {
            R[i]={getnum(),i};
            H[i]=getnum();
        }

        sort(R+1,R+n+1);

        double ans=0;

        for(int i=n;i>=k;i--)
        {
            for(int j=1;j<i;j++)
            {
                A[j]=pi*2.0*R[j].ff*H[R[j].ss];
            }

            sort(A+1,A+i);

            double val = pi*R[i].ff*R[i].ff+pi*2.0*R[i].ff*H[R[i].ss];

            for(int j=1;j<k;j++)
            {
                val+=A[i-j];
            }

            ans=max(ans,val);
        }

        printf("Case #%d: %0.12f\n",cases,ans);
        cerr<<cases<<endl;
    }
}
