#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int F[101][101][101][4];

int t;
int n,p;
int arr[101];

int MAX(int a,int b)
{
    if (a>b)
    return a;
    else
    return b;
}

int Solve(int c1,int c2,int c3,int lst)
{
    if (F[c1][c2][c3][lst]!=-1)
    return F[c1][c2][c3][lst];
    if (c1==0 && c2==0 && c3==0)
    {
        if (lst==0)
        return 0;
        else
        return 1;
    }

    int ans=0;

    if (c1>0)
    {
        if ( (lst+1)%p==0 )
        ans=MAX(ans, Solve(c1-1,c2,c3,0)+1 );
        else
        ans=MAX(ans, Solve(c1-1,c2,c3,(lst+1)%p) );
    }

    if (c2>0)
    {
        if ( (lst+2)%p==0 )
        ans=MAX(ans, Solve(c1,c2-1,c3,0)+1 );
        else
        ans=MAX(ans, Solve(c1,c2-1,c3,(lst+2)%p) );
    }

    if (c3>0)
    {
        if ( (lst+3)%p==0 )
        ans=MAX(ans, Solve(c1,c2,c3-1,0)+1 );
        else
        ans=MAX(ans, Solve(c1,c2,c3-1,(lst+3)%p) );
    }

    F[c1][c2][c3][lst]=ans;

    //cout<<"F["<<c1<<"]["<<c2<<"]["<<c3<<"]["<<lst<<"]="<<ans<<endl;

    return ans;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int i;
    int test;
    int ctrs[4];
    int ans;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        memset(F,-1,sizeof(F));

        scanf("%d %d",&n,&p);

        memset(ctrs,0,sizeof(ctrs));
        for (i=1;i<=n;i++)
        {
            scanf("%d",&arr[i]);

            ctrs[ arr[i]%p ]++;
        }

        ans=Solve(ctrs[1],ctrs[2],ctrs[3],0)+ctrs[0];

        printf("Case #%d: %d\n",test,ans);
    }

    return 0;
}
