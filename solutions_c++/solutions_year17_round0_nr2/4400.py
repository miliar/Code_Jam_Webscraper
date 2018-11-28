#include <bits/stdc++.h>
using namespace std;

string S;
int T;
int main() {
    cin>>T;
    for(int t=1;t<=T;t++){
        cin>>S;
        int l = S.size(), x = l;
        char m = '9';
        for(int i=l-1;i>=0;i--){
            m = min(m, S[i]);
            if(S[i] != m) {
                x = i;
                m = S[i] - 1;
            }
        }
        for(int i=x+1;i<l;i++) S[i] = '9';
        if(x<l){
            if(S[x] == '1') S.erase(S.begin() + x);
            else S[x]--;
        }
        cout<<"Case #"<<t<<": "<<S<<"\n";
    }
    return 0;
}
