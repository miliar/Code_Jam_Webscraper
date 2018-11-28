#include<bits/stdc++.h>

using namespace std;

void solve( int test )
{
    int n,k;
    char str[1010];
    scanf("%s %d",str,&k);
    n = strlen(str);
    int ans = 0;
    for ( int c=0 ; c<n-k+1 ; c++ )
    {
        if ( str[c] == '-' )
        {
            ans++;
            for ( int d=0 ; d<k ; d++ )
            {
                if ( str[c+d] == '+' )  str[c+d] = '-';
                else    str[c+d] = '+';
            }
        }
    }
    for ( int c= n-k+1 ; c<n ; c++ )
    {
        if ( str[c] == '-' )
        {
            printf("Case #%d: IMPOSSIBLE\n",test);
            return ;
        }
    }
    printf("Case #%d: %d\n",test,ans);
}
int main()  {
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for ( int c=1 ; c<=T ; c++ )
    {
        solve(c);
    }
}
