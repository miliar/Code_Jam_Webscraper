#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tt;
    cin >> tt;
    for(int tn = 1; tn <= tt; tn++){
        string s;
        int k;
        cin >> s >> k;
        int n = s.size();
        int f[n];
        memset(f, 0, sizeof f);
        int sw = 0, ans = 0;
        for(int i = 0; i < n-k+1; i++){
            if(s[i] == '-'){
                if(sw % 2 == 0){ // have't done a swap yet so swap it
                    sw++;
                    f[i+k-1] = 1;
                    ans++;
                }
            }else if(s[i] == '+'){ // done a swap before sp swap again back
                if(sw % 2 == 1){
                    sw++;
                    f[i+k-1] = 1;
                    ans++;
                }
            }
            if(f[i]){
                sw--;
            }
        }
        int flag = 0;
        // if i could't swap the last k elements then there are no solution
        for(int i = n-k+1; i < n; i++){
            if(sw % 2 == 1 && s[i] == '+'){
                flag = 1;
            }else if(sw % 2 == 0 && s[i] == '-'){
                flag = 1;
            }
            if(f[i]){
                sw--;
            }
        }
        if(flag){
            cout << "Case #" << tn << ": IMPOSSIBLE" << endl;
        }else{
            cout << "Case #" << tn << ": " << ans << endl;
        }
    }
    return 0;
}
