#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;



string solve() {

    int k;
    string s;
    cin >> s >> k;
    int n = s.size();
    vi hapsad(n);
    rep(i,0,n) {
        if (s[i] == '-') {
            hapsad[i] = 1;
        } else {
            hapsad[i] = 0;
        }
    }
    int ans = 0;
    rep(i,0,n-k+1) {
        if ((hapsad[i]%2) == 1) {
            ans++;
            rep(j,i,i+k) {
                hapsad[j]++;
            }
        }
    }
    rep(i,n-k+1,n) {
        if ((hapsad[i]%2) == 1) {
            return "IMPOSSIBLE";
        }
    }
    return to_string(ans);
}

    
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ": " << solve() << endl;
    }


    return 0;
}
