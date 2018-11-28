#include <bits/stdc++.h>

using namespace std;
typedef long long ll ;


bool f(int n)
{
    int k = n%10 ;
    n/=10 ;
    while ( n )
        if ( (n%10) > k ) return 0 ;
        else k = n%10, n/=10 ;
    return 1;
}
vector < unsigned long long > v;
void gen( unsigned long long s, int cnt )
{
    if ( cnt == 20 ) return ;
    v.push_back(s) ;
    for ( int i = max(1,(int)(s%10)) ; i < 10 ; i++ )
        gen(s*10+i,cnt+1) ;
}
int main()
{
    freopen("B-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    gen(0,0) ;
    sort(v.begin(),v.end()) ;
    int t;
    scanf("%d",&t) ;
    ll n ;
    for ( int ctr = 1 ; ctr <= t ; ctr++ )
    {

        scanf("%I64d",&n) ;
        int idx = upper_bound(v.begin(),v.end(),n) - v.begin() - 1 ;
        printf("Case #%d: %I64d\n",ctr,(ll)v[idx]) ;


    }

    return 0;
}
