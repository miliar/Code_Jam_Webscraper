#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

#define sf scanf
#define pf printf
#define pb push_back
#define mp make_pair
#define PI ( acos(-1.0) )
#define mod 1000000007
#define maxn 100005
#define IN freopen("C.in","r",stdin)
#define OUT freopen("output.txt","w",stdout)
#define FOR(i,a,b) for(i=a ; i<=b ; i++)
#define DBG pf("Hi\n")
#define INF 1000000000000000LL
#define i64 long long int
#define eps (1e-8)
#define xx first
#define yy second
#define ln 17
#define off 2


using namespace __gnu_pbds;
using namespace std ;

typedef tree< i64, null_type, less<i64>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

int main()
{
    i64 i , j , k , l , m , n , t=1 , tc ;

    IN ; OUT ;

    map<i64,i64> M ;
    queue <i64> q ;

    sf("%lld",&tc) ;

    while(t<=tc)
    {
        sf("%lld %lld",&n,&k) ;

        q.push(n) ;
        M[n] = 1 ;

        while(!q.empty())
        {
            m = q.front() ;
            q.pop() ;
            if(M[m] >=k )
            {
                printf("Case #%lld: %lld %lld\n",t++,(m-1) - (m-1)/2,(m-1)/2) ;
                break ;
            }
            else{
                i64 r1 = (m-1)/2 ;
                i64 r2 = (m-1) - r1 ;
                k -= M[m] ;

                if(M.find(r2)==M.end())
                {
                    M[r2] = M[m] ;
                    q.push(r2) ;
                }
                else M[r2] = M[r2] + M[m] ;

                if(M.find(r1)==M.end())
                {
                    M[r1] = M[m] ;
                    q.push(r1) ;
                }
                else M[r1] = M[r1] + M[m] ;
            }
        }
        M.clear() ;

        while(!q.empty()) q.pop() ;
    }

    return 0 ;
}
