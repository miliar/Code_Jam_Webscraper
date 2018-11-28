#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define pi acos(-1.0)
#define rf freopen("in.txt", "r", stdin);
#define ld long double
#define all(v) v.begin(),v.end()
#define pb push_back
#define ff first
#define ss second
#define sz size()
#define ln length()
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define s(n) scanf("%d",&n);
#define sl(n) scanf("%lld",&n);
#define sld(n) scanf("%lf", &n);

using namespace std;

int main() { //rf
                //freopen("out.txt", "w", stdout);
    ll t;
    sl(t);
    for (int x = 1; x <= t; x++) {
        string s;
        ll m, cnt = 0, ans = 0;
        cin >> s; sl(m);

        for (ll i = 0; i < s.length(); i++) {
            if (s[i] == '+') {
                cnt++;
            }
        }

        if (cnt == s.length()) {
           cout << "Case #" << x << ": " << 0 << endl;
            continue;
        }

        cnt = 0;

        for (ll i = 0; i < s.length(); i++) {
            if (s[i] == '-' && i + m <= s.length()) {
                ll j = i;
                cnt = m;
                ans++;
                while (cnt-- && j < s.length()) {
                    if (s[j] == '-') {
                        s[j] = '+';
                        j++;
                    } else {
                        s[j] = '-';
                        j++;
                    }
                }
            }
        }

        cnt = 0;

        for (ll i = 0; i < s.length(); i++) {
            if (s[i] == '+') {
                cnt++;
            }
        }
        //cout << s << endl;
        if (cnt == s.length()) {
            cout << "Case #" << x << ": " << ans << endl;
        }
        else  if (cnt != s.length()){
            cout << "Case #" << x << ": " << "IMPOSSIBLE\n";
        }

    }
    return 0;
}
