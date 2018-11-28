#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=1; i<=t; i++){
        string pan;
        int K;
        cin >> pan >> K;
        int ans = 0;
        for(int j=0; j<=pan.size()-K; j++){
            if(pan[j]=='-'){
                ans++;
                for(int k=j; k<j+K; k++){
                    if(pan[k]=='-') pan[k] = '+';
                    else pan[k] = '-';
                }
            }
        }
        for(int j=0; j<=pan.size(); j++){
            if(pan[j]=='-'){
                ans = 1e9;
                break;
            }
        }
        cout << "Case #" << i << ": ";
        if(ans==1e9) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}
