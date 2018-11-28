#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define ld long double
#define ll long long
#define int long long

using namespace std;

const int MAXN = 101 * 1001 ;


#define cin fin
#define cout fout
ifstream fin ("in.in") ;
ofstream fout ("out.out") ;

///R O Y G B V

///R Y B RY YB RB

int n ;

int a[6] ;

vector<char> v[MAXN] ;

int32_t main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    int t ;
    cin >> t ;
    cout << fixed << setprecision(6) ;
    for(int _ = 1 ; _ <= t ; _ ++ )
    {
        int n ;
        cin >> n ;
        cin >> a[0] >> a[3] >> a[1] >>  a[4] >> a[2] >> a[5] ;
        char ch ;
        int m ;
        bool f = 0  ;
        if(a[0]>a[1]&&a[0]>a[2])
        {
           if(a[0]>a[1]+a[2]) f = 1 ;
           m = a[0] ;
           ch = 'R' ;
           for(int i = 0 ; i < m ; i ++ ) v[i].clear() ;
           int j = 0 ;
           for(int k = 0 ; k < a[1] ; k ++ ) v[j++].push_back('Y') ;
           for(int k = 0 ; k < a[2] ; k ++ )
           {
               j %= m ;
               v[j++].push_back('B') ;
           }
        }
        else if(a[1]>a[2])
        {
            if(a[1]>a[0]+a[2]) f = 1 ;
           m = a[1] ;
           ch = 'Y' ;
           for(int i = 0 ; i < m ; i ++ ) v[i].clear() ;
           int j = 0 ;
           for(int k = 0 ; k < a[0] ; k ++ ) v[j++].push_back('R') ;
           for(int k = 0 ; k < a[2] ; k ++ )
           {
               j %= m ;
               v[j++].push_back('B') ;
           }
        }
        else
        {
            if(a[2]>a[0]+a[1]) f = 1 ;
            ch = 'B' ;
            m = a[2] ;
           for(int i = 0 ; i < m ; i ++ ) v[i].clear() ;
           int j = 0 ;
           for(int k = 0 ; k < a[1] ; k ++ ) v[j++].push_back('Y') ;
           for(int k = 0 ; k < a[0] ; k ++ )
           {
               j %= m ;
               v[j++].push_back('R') ;
           }
        }
        cout << "Case #" << _ << ": " ;
        if(f) cout << "IMPOSSIBLE"  ;
        else{
        for(int i = 0 ; i < m ; i ++ )
        {
            cout << ch ;
            for(auto u : v[i])
                cout << u ;
        }
        }
        cout << '\n' ;
    }
}
