#include <bits/stdc++.h>
using namespace std;
#define ll long long
void solve(int case_no){
    string s;
    ll k,flips = 0;
    cin>>s>>k;
    //cout<<s<<endl;
    for(ll i = 0 ; i < s.size() ;++i){
        if(s[i] == '-'){
        ll pos = 0;

            flips++;
            while(pos<k){
                if((i+pos) == s.size()){
                    cout<<"Case #"<<case_no<<": "<<"IMPOSSIBLE"<<endl;
                    return;
                }
                s[i+pos] = s[i+pos] == '-' ? '+' : '-';
                pos++;
            }
         //cout<<s<<endl;
        }
    }
   // cout<<s<<endl;
    for(auto i:s){
        if(i == '-'){
            cout<<"Case #"<<case_no<<": "<<"IMPOSSIBLE"<<endl;
            return;
        }
    }

    cout<<"Case #"<<case_no<<": "<<flips<<endl;
    return;
}

int main() {
    freopen("largeA.in","r",stdin);
    freopen("outA.txt","w",stdout);
    int T;
    cin>>T;
    int i = 1;
    while(T--) solve(i++);
    return 0;
}