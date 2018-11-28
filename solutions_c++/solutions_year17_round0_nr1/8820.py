#include <iostream>

using namespace std;

typedef long long ll;

int main() {
    ll t;
    cin>>t;
    for(ll Case = 1; Case <= t; Case++) {
        string s;
        ll k;
        cin>>s>>k;
        ll f = 0;
        for(ll i = 0; i < s.size(); i++) {
            if(s[i] == '-' && s.size() - i >= k) {
                for(ll j = 0; j < k; j++) {
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
                }
                f++;
            }
        }
        for(ll i = 0; i < s.size(); i++) {
            if(s[i] == '-') {
                f = -1;
                break;
            }
        }
        cout<<"Case #"<<Case<<": ";
        if(f == -1) {
            cout<<"IMPOSSIBLE\n";
        } else {
            cout<<f<<endl;
        }
    }
    return 0;
}