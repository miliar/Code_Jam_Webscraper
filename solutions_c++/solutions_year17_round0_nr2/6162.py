#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb(x) push_back(x);
#define p(x)    push(x);
#define mp(x, y) make_pair(x, y);
#define f(i,s,n)  for(ll i=s;i<n;++i);
typedef vector< vector<ll> > matrix;
#define inp(x)  scanf("%d",&x);
#define inp( n, x, y)  scanf("%d %d %d",&n, &x, &y);
/*vector <ll> newprime;
void sieve(ll n) {
    ll prime[n]={0};
    //memset(prime, 0, sizeof(prime[n]));
    prime[1] = 1;
    prime[0] = 1;
    for (ll i = 2; i <= n; i++) {
        if (prime[i] == 0) {
            for (ll j = i; i * j <= n; j++) prime[i * j] = 1;
        }
    }
    for (ll i = 2; i <= n; i++) {
        if (prime[i] == 0) {
            newprime.pb(i);
        }
    }
    //for (int i = 0; i < newprime.size(); i++) cout << newprime[i] << " ";
}*/
//xor!=0 first player win
//xor ==0 second player wins

int main() {
    int t, ad, k, d, z, j=1;
    cin >> t;
    string s;
    while (t--) {
        cout<<"Case #"<<j<<": ";
        cin >> s;
        ad = s.size() - 1;
        k = 0;
        string s2, s3;
        for (int i = 0; i < s.size() - 1; ++i) {
            if (s[i + 1] < s[i]) {
                ad = i;
                d = s[i] - '0' - 1;
                break;
            }
        }
        if (ad == s.size() - 1) cout << s << endl;
        else {
            k = ad;
            z = 0;
            while (ad + 1) {
                if (d < s[ad - 1] - '0') {
                    //cout<<d<<" "<<s[ad-1]<<endl;
                    s2 += '9';
                    d = s[ad - 1] - '0' - 1;
                } else {
                    if (z == 0) s2 += to_string(d);
                    else s2 += s[ad];
                    ++z;
                }
                --ad;
            }
            reverse(s2.begin(), s2.end());
            //cout<<s2<<endl;
            for (int i = k + 1; i < s.size(); ++i) s2 += '9';
            for (int i = 0; i < s2.size(); ++i) {
                if (s2[i]-'0' != 0) cout << s2[i];
            }
            cout << endl;
        }
        ++j;
    }
    return 0;
}
