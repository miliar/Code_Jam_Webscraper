#include <bits/stdc++.h>

using namespace std;
 

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int o = 1; o <= T; o++){
        cout << "Case #" << o << ": ";
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int i = 0; i < s.length() - k+1; i++){
            if (s[i] == '-'){
                for (int j = i; j < i+k; j++)
                    if (s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                ans++;
            }
        }
        for (int i = 0; i < s.length(); i++)
            if (s[i] == '-'){
                cout << "IMPOSSIBLE" << endl;
                ans = -1;
                break;
            }
        if (ans != -1){
            cout << ans << endl;
        }
    }   
    return 0;
}
