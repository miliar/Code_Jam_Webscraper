#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    int T;
    freopen("A-large.in","r",stdin);
    freopen("outlarge.txt","w",stdout);
    cin >> T;
    for(int t = 1; t <= T; t++){
        string str;
        cin >> str;
        int k;
        cin >> k;
        int cnt = 0;
        for(int i = 0; i < str.length()-k+1; i++){
            if(str[i] == '+') continue;
            for(int j = 0; j < k; j++){
                if(str[i+j] == '-') str[i+j] = '+';
                else str[i+j] = '-';
            }
            cnt++;
        }
        bool b = true;
        for(int i = 0; i < str.length(); i++){
            if(str[i] == '-'){
                b = false;
                break;
            }
        }
        cout << "Case #" << t << ": ";
        if(b){
            cout << cnt << "\n";
        }
        else{
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
