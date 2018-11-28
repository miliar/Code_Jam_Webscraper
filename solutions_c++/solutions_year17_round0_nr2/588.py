#include <bits/stdc++.h>
using namespace std;

void Solve(int testNum) {
    string num;
    cin >> num;
    string ans = "";
    int ind = -1;
    for(int i = 1; i < num.size(); i++)
        if(num[i-1] > num[i]) { ind = i-1; break; }
    if(ind == -1) {
        printf("Case #%d: ", testNum);
        cout << num << endl;
        return;
    }
    else {
        ans = num;
        int ii = 0;
        for(int i = 0; i < num.size(); i++)
            if(num[i] >= num[ind]) { ii = i; break; }
        ans[ii]--;
        for(ii++; ii < ans.size(); ii++) ans[ii] = '9';
        if(ans[0] == '0') ans = ans.substr(1, ans.size());
    }
    printf("Case #%d: ", testNum);
    cout << ans << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        Solve(i+1);
    }
}
/*
5
134
143
6810
5554
*/
