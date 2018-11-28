#include<bits/stdc++.h>

using namespace std;

void solve ( int t )
{
    int n,p,ans=0,a;
    int co[5];
    scanf("%d%d",&n,&p);
    for ( int c=0 ; c<p ; c++ ) co[c] = 0;
    for ( int c=1 ; c<=n ; c++ )
    {
        scanf("%d",&a);
        co[a%p]++;
    }
    if ( p == 2 )
    {
        ans = co[0] + (co[1]+1)/2;
    }
    else if ( p == 3 )
    {
        int diff = abs(co[1]-co[2]);
        ans = co[0] + min(co[1],co[2]) + (diff+2)/3;
    }
    else
    {
        int diff = abs(co[3]-co[1]);
        ans = co[0];
        int b = co[2] % 2;
        ans += min(co[1],co[3]) + co[2]/2;
        if ( b == 0 )
        {
            ans += (diff+3)/4;
        }
        else
        {
            if ( diff >= 2 )
            {
                diff -= 2;
                ans++;
            }
            ans += (diff+3)/4;
        }
    }
    printf("Case #%d: %d\n",t,ans);
}

int main()  {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for ( int c=1 ; c<=t ; c++ )    solve(c);
}
