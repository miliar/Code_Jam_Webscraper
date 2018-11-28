#include <bits/stdc++.h>

#define ll long long
#define M 1000000007
#define INF 9223372036854775807
#define mp(x, y) make_pair(x,y)
#define pb(x) push_back(x)
#define pmp(x, y) pb(mp(x,y))
#define ld double
#define PI 3.14159265
#define len(a) (ll)a.size()    //
#define F first
#define S second
#define endl "\n"
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;

int main() {

    ll t;
    cin >> t;
    for (ll i = 0; i < t; i++) {
        string s;
        cin >> s;
        ll k;
        cin >> k;

        ll ans=0;
        for (ll j = 0; j <= len(s) - k; j++) {
            if (s[j] == '-') {
                for (ll l = 0; l < k; l++) {
                    if (s[j+l] == '+')
                        s[j+l] = '-';
                    else
                        s[j+l] = '+';
                }
                ans++;
            }
        }

        bool flag=false;
        for (ll j = 0; j < len(s); j++) {
            if(s[j]=='-')
                flag=true;
        }

        cout<<"Case #"<<i+1<<": ";
        if(flag)
            cout<<"IMPOSSIBLE";
        else
            cout<<ans;
        cout<<endl;
    }
    return 0;
}