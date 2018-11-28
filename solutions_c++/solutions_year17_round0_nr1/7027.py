#include<bits/stdc++.h>
#define __SUBMIT__ ios_base::sync_with_stdio(0); \
                   cin.tie(0);
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int MOD = 1e9 + 7;
const int MAX = 1e3;

int main()
{
    __SUBMIT__
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int TC; cin >> TC;
    for (int tc=1; tc<=TC; tc++)
    {
        string s; cin >> s;
        int k; cin >> k;
        bool pancake[MAX+5];
        for (int i=0; i<s.size(); i++) {
            if (s[i] == '+') pancake[i] = true;
            else pancake[i] = false;
        }

        ll ans = 0;
        for (int i=0; i<=s.size()-k; i++) {
            if (!pancake[i]) {
                ans++;
                for (int j=i; j<(i+k); j++) {
                    pancake[j] ^= 1;
                }
            }
        }

        bool flag = true;
        for (int i=0; i<s.size(); i++) {
            if (!pancake[i]) {
                flag = false;
                break;
            }
        }
        if (flag) cout << "Case #" << tc << ": " << ans << "\n";
        else cout << "Case #" << tc << ": IMPOSSIBLE\n";
    }
}
