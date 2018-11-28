/*
	// Author: Suraj Bora
	// Email: surajbora021@gmail.com

*/

#include <bits/stdc++.h>
using namespace std;

int main(){

    int T, n, k;
    string s;

    freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );

    cin >> T;

    cin.ignore();

    for( int t= 1; t<= T; ++t ){

        cin >> s >> k;

        //cout << s << ' ' << k << endl;

        int i= 0;

        n= (int)s.length();

        bool flag= true;
        int cnt= 0;

        while( i < n ){

            if( s[i]== '-' ){
                if( i+k-1 >= n ){
                    flag= false;
                    break;
                }else{
                    for( int j= i; j<= i+k-1; ++j ){
                        if( s[j]== '-' )
                            s[j]= '+';
                        else
                            s[j]= '-';
                    }
                    cnt++;
                }
            }

            i++;
        }

        for( int i= 0; i< n; ++i ){
            if( s[i]== '-' ){
                flag= false;
                break;
            }
        }

        if( !flag ){
            cout << "Case #" << t << ": " << "IMPOSSIBLE\n";
        }else{
            cout << "Case #" << t << ": " << cnt << endl;
        }
    }
}
