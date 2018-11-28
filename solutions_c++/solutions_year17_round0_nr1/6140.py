#include <iostream>

using namespace std;

void flip(char &c)
{
    if(c == '-') c = '+';
    else c = '-';
}

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i){
        string S;
        int K, ans = 0;
        cin >> S >> K;
        for(int j = 0; j < S.size() - (K - 1); ++j){
            if(S[j] == '-'){
                ans++;
                for(int k = 0; k < K; ++k){
                    flip(S[j + k]);
                }
            }
        }
        bool fail = false;
        for(int j = 0; j < S.size(); ++j){
            if(S[j] == '-') fail = true;
        }
        cout << "Case #" << i << ": ";
        if(!fail) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
