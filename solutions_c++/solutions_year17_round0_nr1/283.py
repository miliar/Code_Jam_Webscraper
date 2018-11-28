#include <bits/stdc++.h>

using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ll big = 1000000007ll;
ll big2 = 1000000009ll;
ll n,m,q,T,k;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    cin >> T;
    for(ll c4 = 0; c4 < T; c4++){
        string s;
        cin >> s;
        ll ans = 0;
        bool fail = 0;
        cin >> k;
        for(ll c1 = 0; c1 < s.length()-k+1; c1++){
            if(s[c1] == '-'){
                ans++;
                for(ll c2 = c1; c2 < c1+k; c2++){
                    if(s[c2] == '+'){s[c2] = '-';}else{s[c2] = '+';}
                }
            }
        }
        for(ll c1 = 0; c1 < s.length(); c1++){
            if(s[c1] == '-')fail = 1;
        }
        if(fail == 1){
            cout << "Case #" << c4+1 << ": IMPOSSIBLE\n";
        }
        else{
            cout << "Case #" << c4+1 << ": " << ans << "\n";
        }
    }


    return 0;
}
