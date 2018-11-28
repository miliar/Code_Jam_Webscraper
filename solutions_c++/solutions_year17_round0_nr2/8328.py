#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
string n;
int ans[22];
string res;
int t;

int main() {
    scanf("%d", &t);
    int f = 0;
    while(t--) {
        cin >> n;
        res.clear();
        memset(ans, 0, sizeof ans);
        for(int i = n.size() - 1; i >= 0; i--) {
            if(n[i] < n[i-1] && i >= 1) {
                n[i-1] --;
                for(int j = i; j < n.size(); j++)
                    ans[j] = '9';
            } else
                ans[i] = n[i];
        }
        if(ans[0] != '0') res += ans[0];
        for(int i = 1; i < n.size(); i++) {
            res += ans[i];
        }
        printf("Case #%d: ", ++f);
        cout<<res<<endl;
    }
    return 0;
}
