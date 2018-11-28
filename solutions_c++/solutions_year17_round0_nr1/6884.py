#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 1e5 + 5;
ll a[N];

int main() {
	//ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	int t, l = 0;
	cin >> t;
	while(t--) {
        string s;
        int k, f = 0, ans = 0;
        cin >> s >> k;
        for(int i = 0; i + k <= s.size(); i++) {
            if(s[i] == '-') {
                for(int j = i; j < i + k; j++) {
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
                ans++;
            }
        }
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '-')
                f = 1;
        }
        cout << "Case #" << ++l << ": ";
        if(f == 1) cout << "IMPOSSIBLE\n";
        else cout << ans << "\n";
	}
}
