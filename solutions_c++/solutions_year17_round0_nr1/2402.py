#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        string s; int k;
        cin >> s >> k;

        int ans = 0;
        for (int i = 0; i <= s.length()-k; i++){
            if (s[i] == '-'){
                ans++;
                for (int j = i; j < i+k; j++)
                    s[j] = (s[j] == '-' ? '+' : '-');
            }
        }

        bool ok = true;
        for (int i= 0; i < s.length(); i++)
            if (s[i] == '-'){
                ok = false;
                break;
            }

        cout << "Case #" << cases++ << ": ";
        if (ok){
            cout << ans << endl;
        }
        else{
            cout << "IMPOSSIBLE" << endl;
        }

    }
    return 0;
}
