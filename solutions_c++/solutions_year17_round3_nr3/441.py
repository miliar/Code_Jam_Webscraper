#include<bits/stdc++.h>

using namespace std;

double A[100];

void solve(int t)
{
    int n,k;
    scanf("%d %d",&n,&k);
    double U;
    cin >> U;
    for ( int c=1 ; c<=n ; c++ )    cin >> A[c];
    A[n+1] = 1.0;
    sort(A+1,A+2+n);
    printf("Case #%d: ",t);
    for ( int c=1 ; c<=n ; c++ )
    {
        //printf ("%.3f\n",U);
        if ( (A[c+1]-A[c]) * (c) > U )
        {
            double div = U / c;
            double ans = 1;
            for ( int d=1 ; d<=c ; d++ )    ans *= (A[c]+div);
            for ( int d=c+1 ; d<=n ; d++ )  ans *= A[d];
            printf("%.6f\n",ans);
            return ;
        }
        else    U -= (A[c+1]-A[c]) * (c);
    }
    printf("1.000000\n");
}
int main()  {
    freopen("C-small.in","r",stdin);
    freopen("C-small.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for ( int c=1 ; c<=t ; c++ )    solve(c);
}
