#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const size_t MAX_LEN = 1000;

void flip(char *s, int start, int end){
    while( start != end ){
        if( s[start] == '+')
            s[start] = '-';
        else
            s[start] = '+';
        start++;
    }
}

bool allup(char *s, int start, int end){
    while( start != end ){
        if( s[start] != '+')
            return false;
        start++;
    }
    return true;
}

void solve(int n_case){
    char s[MAX_LEN+5] = {0};
    int k;

    cin >> s >> k;

    int n = strlen(s);

    int ans = 0;
    for( int i=0; i != n-k+1; i++){
        cerr << i << "\t" << s;
        if( s[i] == '-'){
            ans++;
            flip(s, i, i+k);
        }
        cerr << "\t" << s << "\n";
    }
    if( allup(s, n-k, n) ){
        cout << "Case #" << n_case << ": " << ans << "\n";
    }else{
        cout << "Case #" << n_case << ": IMPOSSIBLE\n";
    }
}

int main(){
    int T;
    cin >> T;
    for( int t = 1; t <= T; t++){
        solve(t);
    }
    return 0;
}
