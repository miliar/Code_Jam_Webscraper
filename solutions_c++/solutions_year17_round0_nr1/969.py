#include<bits/stdc++.h>

#define show(x) cout << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<double, ii> iii;

const int MAX = 200005;
const double EPS = 1e-5;
const int INF = INT_MAX;

int cases;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    #ifdef FSOCIETY
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // FSOCIETY

    int t; cin >> t;
    while(t--) {
        string s; cin >> s;
        int k; cin >> k;
        int ans = 0, sum = 0;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '-') {
                ans++;
                if(i+k <= s.size()) {
                    for(int j = i; j < i+k; j++) {
                        if(s[j] == '-') s[j] = '+';
                        else s[j] = '-';
                    }
                }
            }
            if(s[i] == '+') sum++;
        }

        if(sum == s.size()) cout << "Case #" << ++cases << ": " << ans << "\n";
        else cout << "Case #" << ++cases << ": IMPOSSIBLE\n";
    }

}
