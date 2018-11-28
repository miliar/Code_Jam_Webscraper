#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;
    int csT = 0;
    while (T--){
        string s;
        int n;
        cin >> s >> n;
        int slen = s.length();
        int ans = 0;
        for(int i = 0; i < slen - n; i++){
            if(s[i] == '-'){
                ans ++ ;
                for(int j = 0; j < n; j++){
                    if(s[i+j] == '-')
                        s[i+j] = '+';
                    else
                        s[i+j] = '-';
                }
            }
        }
        int flag = 0;
        for(int i = slen-n + 1; i < slen; i++){
            if(s[i] != s[slen-n]){
                flag = 1;
                break;
            }
        }
        if(flag == 1)
            cout << "Case #"<< ++csT << ": IMPOSSIBLE" << endl;
        else{
            if(s[slen-1] == '-'){
                ans += 1; 
            }
            cout << "Case #"<< ++csT << ": " << ans << endl;
        }
    }
    return 0;
}
