#include<bits/stdc++.h>

using namespace std;



void solve( int t )
{
    int n,dis;
    cin >> dis >> n;
    double mxtime=0,speed,position,tim;
    for ( int c=1 ; c<=n ; c++)
    {
        cin >> position >> speed;
        tim = (dis-position)/speed;
        mxtime = max(mxtime,tim);
    }
    printf("Case #%d: %.6f\n",t,(double)dis/mxtime);
}

int main()  {
    freopen("A-large.in","r",stdin);
    freopen("A-large_out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for ( int t=1 ; t<=T ; t++ )
    {
        solve(t);
    }
}
