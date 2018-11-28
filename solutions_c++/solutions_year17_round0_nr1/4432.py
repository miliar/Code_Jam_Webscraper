#include <bits/stdc++.h>
using namespace std;

string S;
int K;
int main() {
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int ans = 0;
        cin>>S>>K;
        for(int i=0; i<S.size() && ans!=-1; i++){
            if(S[i] == '-'){
                ans++;
                for(int j=i;j<=i+K-1;j++){
                    if(j>=S.size()){
                        ans=-1;
                        break;
                    }
                    S[j] = '+' + '-' - S[j];
                }
            }
        }
        if(ans == -1)
            cout<<"Case #"<<t<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<t<<": "<<ans<<"\n";
    }
    return 0;
}
