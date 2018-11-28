#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

string solve(){
    string s;
    cin >> s;

    int len = s.size();
    if( len == 1 ){
        return s;
    }

    int idx = 0, midx = 0;
    int i;

    for( i = 1; i < len ; i++){
        if( s[i] > s[i-1] ){
            midx = i;
            idx = i;
        }else if( s[i] == s[i-1] ){
            idx = i;
        }else{
            break;
        }
    }
    if ( idx != len - 1 ){
        s[midx]--;
        fill(s.begin()+midx+1, s.end(), '9');
    }
    return s;
};


int main(){
    int T;
    scanf("%d", &T);
    for( int t=1; t<=T; t++){
        const char *ans = solve().data();
        if( ans[0] == '0' ) ans++;
        printf("Case #%d: %s\n", t, ans );
    }
}
