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
    long long n;
    cin >> n;
    long long ans = 1;
    vector<int> ch = parse(n);
    long long cur = 0;
    for (int i = 0; i < ch.size(); i++){
        if (ch[i] != 0)
        if (i == 0 || ch[i] - 1 >= ch[i - 1]){
            cur = 0;
            for (int j = 0; j <= i; j++){
                cur *= 10;
                cur += ch[j];
            }
            cur--;
            for (int j = i + 1; j < ch.size(); j++){
                cur *= 10;
                cur += 9;
            }
            ans = max(ans, cur);
        }
        if (i != 0 && ch[i] < ch[i - 1]) break;
    }
    {
        bool f = true;
        for (int i = 1; i < ch.size(); i++){
            if (ch[i] < ch[i - 1]){
                f = false;
            }
        }
        if (f) ans = n;
    }
    cout << "Case #" << kek << ": " << ans << endl;
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
