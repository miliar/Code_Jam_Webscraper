#include<bits/stdc++.h>
using namespace::std;
string Compute(string s){
    bool found=false;
    int i;
    for(i=0;i<s.size()-1;i++){
        if(s[i]>s[i+1]) {
                found = true;
                break;
        }
    }
    if(found){
        while(i>=1 && s[i]==s[i-1]) i--;
        s[i]=s[i]-1;
        for(int j=i+1;j<s.size();j++) s[j]='9';
    }
    while(s.size() && s[0]=='0') s.erase(s.begin());
    return s;
}

int main(){
    int T;
    string N;
    cin >> T;
    for(int tt=1;tt<=T;tt++){
        cin >> N;
        string res = Compute(N);
        cout  << "Case #" << tt << ": " << res << endl;
    }
    return 0;
}

