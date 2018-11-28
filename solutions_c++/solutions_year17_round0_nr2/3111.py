#include <bits/stdc++.h>

using namespace std;
string s;
int main(){

    freopen("tugfa.in","r",stdin);
    freopen("entanga.out","w",stdout);

    int tc; cin >> tc;
    int c = 0;
    while( tc-- ){
        cin >> s;
        s = '0'+s;
        for( int i = 1 ; i < (int)s.size() ; ++i ){
            if( s[i] < s[i-1] ){
                s[i-1]--;
                for( int j = i ; j < (int)s.size() ; ++j ){
                    s[j] = '9';
                }
                i-=2;
            }
        }
        cout << "Case #" << ++c << ": ";
        int p = 0;
        while( s[p] == '0' ) p++;
        for( int i = p ; i < (int)s.size() ; ++i ){
            cout << s[i];
        }cout << '\n';
    }

}
// 0989999999989
