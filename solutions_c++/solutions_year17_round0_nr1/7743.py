#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int t, k;
    string s;
    cin>>t;
    for(int tc = 1; tc <= t; tc++){
        cin>>s>>k;
        int cnt = 0;
        bool possible = true;
        for(int i = 0; i < s.size() - k + 1; i++){
            //cout<<s<<endl;
            if(s[i] == '-'){
                cnt++;
                for(int j = i; j < i + k; j++){
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '-'){
                possible = false;
                break;
            }
        }
        cout<<"Case #"<<tc<<": ";
        if(possible)cout<<cnt;
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    return 0;
}
