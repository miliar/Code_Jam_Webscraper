#include <bits/stdc++.h>

using namespace std;
string s;
void conv( int a, int b ){

    for( int i = a ; i <= b ; ++i ){
        if( s[i] == '+' ){
            s[i] = '-';
        }else{
            s[i] = '+';
        }
    }

}

int main(){

    freopen("lolzano1.in", "r", stdin);
    freopen( "lolzano.out", "w", stdout );

    int tc; cin >> tc;
    int c = 0;
    while( tc-- ){
        cin >> s;
        string aux = string( (int)s.size(), '+' );
        int n, ans = 0; cin >> n;

        for( int i = 0 ; i < (int)s.size() - (n-1) ; ++i ){
            if( s[i] == '-' ){
                conv(i,i+(n-1));
                ans++;
            }
        }


        cout << "Case #" << ++c << ": ";
        if( s != aux ){
            cout << "IMPOSSIBLE\n";
        }else{
            cout << ans << '\n';
        }

    }

}
