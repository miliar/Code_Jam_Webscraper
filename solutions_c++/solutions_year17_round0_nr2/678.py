#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<int> a, ans;

bool dfs(int i, int now, int n) {
    if(i == n) {
        if(a[i]<now) return false;
        ans.push_back(a[i]);
        return true;
    }
    if(a[i]<now) return false;
    ans.push_back(a[i]);
    if(dfs(i+1, a[i], n)) {
        return true;
    }
    ans.pop_back();
    if(a[i] == 0 || a[i]-1<now) return false;
    ans.push_back(a[i]-1);
    for(int j = i+1; j <= n; j ++) {
        ans.push_back(9);
    }
    return true;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase ++) {
        ll n;
        cin >> n;
        a.clear();
        ans.clear();
        while(n) {
            a.push_back(n % 10);
            n /= 10;
        }
        reverse(a.begin(), a.end());
        dfs(0, 0, a.size() - 1);
        ll ret = 0;
        for(int i = 0; i < ans.size(); i ++) {
            ret = ret * 10 + ans[i];
        }
        printf("Case #%d: ", kase);
        cout << ret << endl;
    }
    return 0;
}
