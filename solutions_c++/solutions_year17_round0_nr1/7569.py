#include <bits/stdc++.h>

using namespace std;

int main(){
    int i,j,k,l,m,n,test,t;
    string s;
    cin >> test;
    for (t = 0; t < test; t++){
        cin >> s >> k;
        n = s.length();
        int ans = 0;
        cout << "Case #" << t + 1 << ": ";
        for (i = 0; i < n - k + 1; i++){
            if (s[i] == '-'){
                ans++;
                for (j = i; j < i + k; j++){
                    if (s[j] == '-') s[j] = '+'; else s[j] = '-';
                }
            }
        }
        int d = 1;
        for (i = n - k + 1; i < n; i++){
            if (s[i] == '-'){
                d = 0;
                break;
            }
        }
        if (d) {
            cout << ans << "\n";
        } else{
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
