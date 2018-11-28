#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("C:\\Users\\Bibin\\Downloads\\A-large.in", "r", stdin);
    freopen("C:\\Users\\Bibin\\Downloads\\output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
        string S;
        int K;
        cin >> S >> K;
        vector<int> s(S.size());
        for(int i=0; i<S.size(); i++){
            if(S[i] == '+'){
                s[i] = 1;
            }else{
                s[i] = -1;
            }
        }

        int f=0;
        bool b=true;
        int c=0;
        while(f<s.size() && s[f] == 1){
            f++;
        }

        while(b && f<s.size()){
            for(int i=f; i< f+K; i++){
                if(i == s.size()){
                    b = false;
                    break;
                }
                s[i] = -s[i];
            }
            while(f<s.size() && s[f] == 1){
                f++;
            }
            c++;
        }

        cout << "Case #" << t << ": ";
        if(b){
            cout << c;
        }else{
            cout << "IMPOSSIBLE";
        }
        cout << "\n";
    }
}
