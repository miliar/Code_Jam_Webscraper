#include <bits/stdc++.h>
#include <sys/unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#define ll  long long
#define f first
#define s second  
#define pii pair< ll,ll > 
#define pb push_back
#define sc(x) scanf("%d",&x)
#define lw lower_bound
#define llmax 1e9
#define mod 1000000007
#define block 350
#define MAX 500010
#define set < ll > Set 
using namespace std;

priority_queue <pii,vector<pii> > pq ;
map <ll,ll> mii ,mii1 ;
map <ll,ll> ::iterator iit,iit1;
map <string ,ll> msi ;
map <string ,ll> ::iterator sit ;
map <char ,ll > mci ;
map <char ,ll > ::iterator cit ;
map <ll ,bool > mark ;
map <ll ,bool > ::iterator bit ;
vector <char > v[3] ;
vector <ll > ::iterator vit ;
map < pii ,ll > mp ,mp1;
map < pii ,ll > ::iterator it ,tit ,it1 ;
map < pii ,ll > grundy ;
string s ;

int  main  () {
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int fdw1 = open ("inputf.in",0666) ;
    dup2 (fdw1,0) ;
    int fdw =open ("outputf.in",0666|O_TRUNC) ;
    dup2 (fdw,1) ;
    int t ;
    cin >> t ;

    for ( int q =1 ;q <= t ;q++ ) {
        int k ,ans =0 ;
        cin >>s >>k ;
        bool flag =true ;
        int n =s.length () ;
        for ( int i =0 ; i < n; i++) {
            if ( s [i] == '-') {
                {
                    ans ++ ;
                if ( i+k > n ) {
                    flag =false ; 
                    break;
                    }
                }
                for ( int j = i ; j < i+k && j < n ; j++ ) {
                    if ( s[j] == '+') s[j] ='-' ;
                    else s[j] = '+' ;
                }
            }
            // cout << s << "\n" ;
        }
        if ( flag )
        cout <<"Case #"<<q<<": "<< ans<<"\n";
        else 
        cout <<"Case #"<<q<<": "<< "IMPOSSIBLE"<<"\n";   
    }
}

/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/