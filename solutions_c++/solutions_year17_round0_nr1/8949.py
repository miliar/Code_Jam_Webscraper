#include<bits/stdc++.h>
using namespace std;

int T,K;
string S;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-ans.txt", "w", stdout);

    cin >> T;

    for(int i=0;i<T;i++){
        cin >> S >> K;

        int ans = 0;
        for(int j=0;j<=S.size()-K;j++){
            if(S[j]=='-'){
                ans++;
                for(int k=0;k<K;k++){
                    if(S[j+k]=='+') S[j+k] = '-';
                    else            S[j+k] = '+';
                }
            }
        }

        bool fail = false;
        for(int j=S.size()-K+1;j<S.size();j++){
            if(S[j]=='-') fail = true;
        }

        if(fail) cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << '\n';
        else     cout << "Case #" << i+1 << ": " << ans << '\n';
    }

    return 0;
}
