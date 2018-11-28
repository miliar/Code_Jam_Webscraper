#include<iostream>
using namespace std;
int main() {
    int T;
    int K, S;
    string s;
    cin>>T;
    for(int t=1; t<=T; t++) {
        cin>>s>>K;
        S = s.size();
        int cnt = 0;
        for(int i=0; i<S-K+1; i++) {
            if(s[i]=='-') {
                cnt++;
                for(int j=i; j<i+K; j++) {
                    if(s[j]=='-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
        bool poss = true;
        for(int j=0; j<S; j++) {
            if (s[j] == '-') {
                poss = false;
                break;
            }
        }
        if(!poss) {
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        }else {
            cout<<"Case #"<<t<<": "<<cnt<<endl;
        }
    }
    return 0;
}