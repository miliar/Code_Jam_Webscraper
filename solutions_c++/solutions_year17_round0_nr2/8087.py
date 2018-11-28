#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll conv(string s){
    ll n = 0;
    for(auto i : s){
        n = n*10 + (i-'0');
    }
    return n;
}




void solve(ll case_no){
    string s;
    cin>>s;
    ll n = s.size();
    ll k = conv(s);
    if(n == 1){
        cout<<"Case #"<<case_no<<": "<<s<<endl;
        return;
    }
    for(ll i = n-2 ; i >= 0; i--){
        if(s[i] > s[i+1]){
            s[i] = s[i] == '0' ? '9' : s[i]-1;
            s[i+1] = '9';
            if (i <= n-3)
                if(s[i+1] > s[i+2]){
                    ll pos = i;
                    while(s[pos+1] > s[pos+2] && pos+2<n){
                        s[pos+2] = '9';
                        pos++;
                    }
                }
        }
    }
    cout<<"Case #"<<case_no << ": "<<conv(s)<<endl;
}


int main() {
    freopen("Blarge.in","r",stdin);
    freopen("outB.txt","w",stdout);
    int T;
    cin>>T;
    ll i = 1;
    while(T--)
        solve(i++);
    return 0;
}