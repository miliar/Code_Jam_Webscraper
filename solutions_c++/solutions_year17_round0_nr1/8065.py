#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("OutputA.txt", "w", stdout);

    int T;
    cin>>T;
    string S;   int K;
    for(int i=1;i<=T;i++){
        cin>>S; cin>>K;
        int limit = S.length()-K;
        int c = 0;
        for(int j=0; j<=limit; j++){
            if(S[j] == '+')
                continue;
            c++;
            for(int m=j; m<(j+K); m++)
                S[m] = S[m]=='-'? '+':'-';
        }

        bool impossible = false;
        for(int m=limit; m<(limit+K); m++){
            if(S[m] == '-'){
                cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
                impossible = true;
                break;
            }
        }
        if(!impossible)
            cout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}

