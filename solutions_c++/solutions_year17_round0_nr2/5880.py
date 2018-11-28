#include <bits/stdc++.h>

using namespace std;

string n, ans;

bool solve(string llevo, int i, bool any) {
    if(llevo.size() > 1 && llevo[llevo.size() - 2] > llevo[llevo.size() - 1])   return false;
    if(llevo.size() == n.size()) {
        ans = llevo;
        return true;
    }
    if(any)
        return solve(llevo + '9', 1 + i, true);
    if(solve(llevo + n[i], 1 + i, any))
        return true;
    return solve(llevo + char(n[i] - 1), i, true);
}

int main() {
    int c;
    cin >> c;
    for(int p = 1 ; p <= c ; ++p) {
        cin >> n;
        solve("", 0, false);
        cout << "Case #" << p << ": ";
        for(int i = 0 ; ; ++i)
            if(ans[i] != '0') {
                for(int j = i ; j < ans.size() ; ++j)
                    cout << ans[j];
                break;
            }
        cout << endl;
    }
    return 0;
}
