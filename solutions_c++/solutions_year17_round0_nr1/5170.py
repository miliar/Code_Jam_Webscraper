#include<bits/stdc++.h>
using namespace std;

int k;
string s;

int trans(string s){
    int i = 0;
    for( ; i < s.size(); i++)
        if(s[i] != '+')
            break;
    if(i == s.size())
        return 0;
    if(s.size() < k)
        return 0x3f3f3f3f;

    if(s[s.size()-1] != '+'){
        for(int i = 0; i < k ; i++)
            s[s.size()-1-i] = s[s.size()-1-i] == '+' ? '-' :'+';
        return 1+trans(s.substr(0, s.size()-1));
    }
    return trans(s.substr(0, s.size()-1));
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> s >> k;
        int cnt = trans(s);
        if(cnt <= s.size())
            printf("Case #%d: %d\n", i, cnt);
        else
            printf("Case #%d: %s\n", i, "IMPOSSIBLE");
    }
    return 0;
}
