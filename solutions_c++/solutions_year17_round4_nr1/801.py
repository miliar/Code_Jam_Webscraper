#include <bits/stdc++.h>

using namespace std;

typedef long long ll ;

int dp2[111][111] ;
int dp3[111][111][111] ;
int dp4[111][111][111][111] ;
int x;int p ;int n ;
int f2(int ones, int rem)
{
    if ( !ones ) return 0 ;
    if ( dp2[ones][rem] != -1 ) return dp2[ones][rem] ;
    int ans = !rem + f2(ones-1, (rem+1)%p) ;
    return dp2[ones][rem] = ans ;
}
int f3(int ones, int twos, int rem)
{
    if ( !ones && !twos ) return 0 ;
    if ( dp3[ones][twos][rem] != -1 ) return dp3[ones][twos][rem] ;
    int ans = 0 ;
    if ( ones )
        ans = max(ans,!rem + f3(ones-1, twos, (rem+2)%p)) ;
    if ( twos)
        ans = max(ans, !rem + f3(ones,twos-1, (rem+1)%p)) ;
    return dp3[ones][twos][rem] = ans ;
}
int f4(int ones, int twos, int threes, int rem)
{
    if ( !ones && !twos && !threes ) return 0 ;
    if ( dp4[ones][twos][threes][rem] != -1 ) return dp4[ones][twos][threes][rem] ;
    int ans = 0 ;;
    if (ones)
        ans = max(ans,!rem + f4(ones-1, twos,threes ,(rem+3)%p)) ;
    if ( twos )
        ans = max(ans, !rem + f4(ones,twos-1,threes, (rem+2)%p)) ;
    if ( threes )
        ans = max(ans, !rem + f4(ones,twos,threes-1, (rem+1)%p)) ;
    return dp4[ones][twos][threes][rem] = ans ;
}
int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    int t ;
    scanf("%d",&t) ;
    int ans ;
    for ( int ctr = 1 ; ctr <= t ; ctr++ )
    {
        ans = 0 ;
        scanf("%d%d",&n,&p) ;
        int cnt[10] = {} ;
        for ( int i = 0 ; i < n ; i++ )
        {
            scanf("%d",&x) ;
            if ( x % p == 0 )
                ans++ ;
            else
                cnt[x%p]++ ;
        }
        if ( p == 2 )
        {
            memset(dp2,-1,sizeof dp2) ;
            ans += f2(cnt[1],0) ;
        }
        else if ( p == 3 )
        {
            memset(dp3,-1,sizeof dp3) ;
            ans += f3(cnt[1],cnt[2],0) ;
        }
        else
        {
            memset(dp4,-1,sizeof dp4) ;
            ans += f4(cnt[1],cnt[2],cnt[3],0) ;
        }
        printf("Case #%d: %d\n",ctr,ans) ;
    }

    return 0;
}
