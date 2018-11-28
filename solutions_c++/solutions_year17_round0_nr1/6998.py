#include<iostream>
using namespace std;
int main() {
    int t,k;
    string s;
    cin>>t;
    for (int i=1;i<=t;i++) {
        cin>>s>>k;
        string tmp = "";
        int cnt = 0;
        for(int j=0;j<s.size();j++) {
            tmp+='+';
        }
        for(int j=0;j<s.size()-k+1;j++) {
            if (s[j] == '-') {
                for(int x=0;x<k;x++) {
                    if (s[x+j] == '-') s[x+j] = '+';
                    else s[x+j] = '-';
                }
                cnt++;
            }
        }
        cout<<"Case #"<<i<<": ";
        if (s == tmp) {
            cout<<cnt<<endl;
        } else {
            cout<<"IMPOSSIBLE"<<endl;
        }
    }

}

