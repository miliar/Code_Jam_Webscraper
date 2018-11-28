#include <bits/stdc++.h>

using namespace std;

string S;
int k;

char Change(char p){
    if(p == '+')    return '-';
    return '+';
}

bool Check(){
    for(int i=0; i<S.size(); i++){
        if(S[i] == '-') return false;
    }
    return true;
}

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int _=1; _<=T; _++){
        cout << "Case #" << _ << ": ";

        int ans = 0;
        cin >> S >> k;
        for(int i=0; i<=S.size()-k; i++){
            if(S[i] == '-'){
                for(int j=i; j<i+k; j++)
                    S[j] = Change(S[j]);
                ans++;
            }
        }

        if(Check()){
            cout << ans << endl;
        }
        else{
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
