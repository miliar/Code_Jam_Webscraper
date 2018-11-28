#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define eb emplace_back

const int N = 1010;

vector<int> parse(long long n){
    vector<int> ans;
    while (n > 0){
        ans.push_back(n % 10);
        n /= 10;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

void solve(int kek){
    cout << "Case #" << kek << ": ";
    ///
    string s;
    int k;
    cin >> s >> k;
    int ans = 0;
    for (int i = 0; i < s.size() - k + 1; i++){
        if (s[i] == '-'){
            ans ++;
            for (int j = i; j < i + k; j++){
                if (s[j] == '-'){
                    s[j] = '+';
                }
                else{
                    s[j] = '-';
                }
            }
        }
    }
    for (int i = 0; i < s.size(); i++){
        if (s[i] == '-') ans = -1;
    }
    if (ans == -1){
        cout << "IMPOSSIBLE" << endl;
    }
    else{
        cout << ans << endl;
    }
}
int main() {
    ios_base::sync_with_stdio(0);
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        solve(i);
    }
    return 0;
}
