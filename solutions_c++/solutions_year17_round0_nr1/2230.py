#include <iostream>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        string S;
        int K;
        cin>>S>>K;
        int ans = 0;
        for(int i=0;i+K<=S.size();i++){
            if(S[i]=='-'){
                ans++;
                for(int j=i;j<i+K;j++){
                    if(S[j]=='-') S[j]='+';
                    else S[j]='-';
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        int cnt = 0;
        for(auto c:S) cnt+=c=='+';
        if(cnt!=S.size()) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }


    return 0;
}