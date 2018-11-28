#include <bits/stdc++.h>
using namespace std;

void flip(string& str, int idx){
    if(str.at(idx) == '-') str.at(idx) = '+';
    else str.at(idx) = '-';
}

int main(void){
    int T; cin >> T;
    for(int Case = 0; Case < T; Case++){
        int ans = 0;
        string str; cin >> str;
        int K; cin >> K;
        for(int i = 0; i < str.size() - K + 1; i++){
            if(str.at(i) == '-'){
                ans++;
                for(int j = 0; j < K; j++){
                    flip(str, i+j);
                }
            }
        }

        cout << "Case #" << Case+1 << ": ";
        bool flg = true;
        for(int i = 0; i < str.size(); i++){
            if(str.at(i) == '-'){
                flg = false;
            }
        }
        if(flg){
            cout << ans << endl;
        }else{
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
