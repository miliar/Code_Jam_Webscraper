#include <bits/stdc++.h>
using namespace std;






int main() {
    freopen("inputA","r",stdin);
    freopen("outputA","w",stdout);
    int tests;
    cin>>tests;
    string s;
    int k;
    for (int T = 1; T <= tests; ++T) {
        cin>>s>>k;
        if(s.length()<k){
            cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<endl;

        }
        int num=0;
        bool isReal=true;
        for (int i = 0; i <= s.length()-k; ++i) {
            if(s[i]=='+') continue;
            num++;
            s[i]='+';
            for (int j = i+1; j <= i+k-1; ++j) {
                if(s[j]=='-') s[j]='+';
                else s[j]='-';
            }
        }
        for (int i = s.length()-k+1; i < s.length(); ++i) {
            if(s[i]=='-'){
                isReal=false;
                break;
            }
        }
        if(isReal) cout<<"Case #"<<T<<": "<<num<<endl;
        else cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<endl;


    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
