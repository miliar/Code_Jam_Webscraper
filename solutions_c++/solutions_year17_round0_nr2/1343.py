#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t, ans, f, i, j, l;
string s;
int main() {
    cin>>t;
    for(ll _t = 1; _t <= t; _t++) {
        cin>>s;
        l = s.length();
        f = 0;
        for(i = 0; i < l-1; i++) {
            if(s[i] == s[i+1]) continue;
            if(s[i] > s[i+1]) {
                s[f] = s[f]-1;
                for(j = f+1; j < l; j++) s[j] = '9';
                break;
            }
            if(s[i] != s[i+1]) f = i+1;
        }
        ans = stoll(s);
        printf("Case #%lld: %lld\n", _t, ans);
    }

    return 0;
}
