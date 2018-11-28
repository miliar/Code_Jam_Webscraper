//
#include <bits/stdc++.h>
//StAn_
using namespace std ;

#define nl cout<<endl;
#define pb push_back
#define MAX 100005
#define FOR(i,start,end) for(int i=start;i<end;i++)
typedef long long ll ;

ll to_ll( string s )
{
    ll ans = 0 ;
    for(char ch : s)
    {
        ans = ans*10 + (ch - '0') ;
    }
    return ans;
}


ll dodo ( string s )
{
    ll len = s.length() ;

    bool is_sam[len] ;
    memset(is_sam, false, sizeof(is_sam)) ;

    FOR(i, 1, len)
    {
        if(s[i] == s[i-1])
            is_sam[i] = true ;
        if(s[i] < s[i-1])
        {
            ll j;
            for(j=i-1; j>=1; j--)
            {
                if(!is_sam[j])
                    break ;
            }
            i = j+1;
            s[i-1] -= 1 ;
            FOR(j, i, len)
            {
                s[j] = '9' ;
            }
            return to_ll(s) ;
        }
    }

    return to_ll(s) ;
}



int main()
{
      #ifndef ONLINE_JUDGE
            freopen( "sm.txt", "r", stdin ) ;
            freopen( "smo.txt", "w", stdout ) ;
      #endif
      std::ios_base::sync_with_stdio( false ) ;
//_________________________________________________________________

      ll Test, i ;
      cin>>Test ;
      FOR(T,1,Test+1)
      {
            ll n, m, ans ;
            string s ;
            cin>>s ;

            ans = dodo( s ) ;

            cout<<"Case #"<<T<<": "<<ans <<endl ;
      }

      return 0;
}
