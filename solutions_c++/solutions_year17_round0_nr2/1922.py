#include <bits/stdc++.h>

using namespace std;

int dp[20][10][2];
string s;
int solve(int x, int last, bool equ) {
    if(x == s.size()) {
        return 1;
    }
    int &ret = dp[x][last][equ];
    if(ret != -1) return ret;
    ret = 0;
    if(x == 0) {
        for(int i = 0; i < 10; i++) {
            if(i > s[0]-'0') break;
            else if(i == s[0] - '0') {
                ret = max(ret, solve(x+1, i, 0));
            } else {
                ret = max(ret, solve(x+1, i, 1));
            }
        }
    } else {
        for(int i = last; i < 10; i++) {
            if(!equ) {
                if(i > s[x]-'0') break;
                else if(i == s[x]-'0') {
                    ret = max(ret, solve(x+1, i, 0));
                } else{
                    ret = max(ret, solve(x+1, i, 1));
                }
            } else{
                ret = max(ret, solve(x+1, i, 1));
            }
        }
    }
    return ret;
}

void trace(int x, int last, bool equ, string &ans) {
    if(x == s.size())return;
    if(x == 0) {
        for(int i = 9; i >= 0; i--) {
            if(i > s[0]-'0') continue;
            else if(i == s[0] - '0') {
                if(!solve(x+1, i, 0))continue;
                ans += char(i+'0');
                trace(x+1, i, 0, ans);
                return;
            } else {
                if(!solve(x+1, i, 1))continue;
                ans += char(i+'0');
                trace(x+1, i, 1, ans);
                return;
            }
        }
    } else {
        for(int i = 9; i >= last; i--) {
            if(!equ) {
                if(i > s[x]-'0') continue;
                else if(i == s[x] - '0') {
                    if(!solve(x+1, i, 0))continue;
                    ans += char(i+'0');
                    trace(x+1, i, 0, ans);
                    return;
                } else {
                    if(!solve(x+1, i, 1))continue;
                    ans += char(i+'0');
                    trace(x+1, i, 1, ans);
                    return;
                }
            } else{
                if(!solve(x+1, i, 1))continue;
                ans += char(i+'0');
                trace(x+1, i, 1, ans);
                return;
            }
        }
    }
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for(int I = 1; I <= t; I++){
        long long x;
        cin >> x;
        s = to_string(x);
        memset(dp,-1,sizeof dp);
        solve(0, 0, 0);
        string ans = "";
        trace(0, 0, 0, ans);
        reverse(ans.begin(),ans.end());
        while(ans.back() == '0') ans.pop_back();
        reverse(ans.begin(), ans.end());
        printf("Case #%d: ", I);
        cout << ans << "\n";
    }
    return 0;
}
