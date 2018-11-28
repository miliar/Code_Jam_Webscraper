#include<bits/stdc++.h>
using namespace std;

string f() {
    string s;
    cin>>s;
    

    string t(s.size(),'1');
    if(t>s) return string(s.size()-1,'9');
    char lowest = '1';
    for(int i=0;i<s.size();i++) {
        for(char c = lowest; c <= '9'; c++) {
            string tt = t;
            for(int j=i;j<s.size();j++) tt[j]=c;
            if(tt<=s) {
                t=tt;
                lowest = c;            
            }
        }
    }
    return t;

}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        auto s = f();
        cout<<"Case #"<<i<<": "<<s<<endl;

    }
}
