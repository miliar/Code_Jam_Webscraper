#include <iostream>
#include <string.h>
#include <map>
using namespace std;

int t;
#define rr 1000000007

void count (string s, int now, string ans) {
    int len = ans.size();
    if (now == -1) {
        int i;
        for (i=len-1; i>=1 && ans[i] == '0'; i--);
        
        if (i == 0)
            cout << '0' << endl;
        
        for (; i>=1; i--)
            cout << ans[i];
        cout << endl;
        return;
    }
    
    int l = ans.size()-1;
    if (s[now] <= ans[l]) {
        ans.append(1, s[now]);
        count (s, now-1, ans);
    }
    else {
        ans.append(1, char(s[now] - 1));
        for (int i=1; i<len; i++)
            ans[i] = '9';
        count (s, now-1, ans);
    }
}

void solve () {
    string s;
    cin >> s;
    string ans = "9";
    int len = s.size();
    count(s, len-1, ans);
}


int main () {
    cin >> t;
    int tmp  = 1;
    while (t--) {
        cout << "Case #" << tmp << ": ";
        solve();
        tmp ++;
    }
                        
}