#include <bits/stdc++.h>

using namespace std;

void flipRange(string& row, int left, int K) {
    for(int i=left;i<left+K;++i)
        row[i] = row[i] == '+' ? '-' : '+';
}

int solve(const string& row, int K) {
    int ans = 0;
    string rowcpy(row);
    for(int i=0;i<rowcpy.size()-K+1;++i) {
        if(rowcpy[i] == '-') {
            flipRange(rowcpy, i, K);
            ans++;
        }
    }

    for(int i=0;i<rowcpy.size();++i)
        if(rowcpy[i] == '-')
            return -1;
    return ans;
}

int main() {
    int tc;
    cin >> tc;
    for(int ii=1;ii<=tc;++ii) {
        string row;
        int K;
        cin >> row >> K;

        int ans = solve(row, K);
        reverse(row.begin(), row.end());
        int ans2 = solve(row, K);

        cout << "Case #" << ii << ": ";
        if(ans == -1 && ans2 == -1)
            cout << "IMPOSSIBLE" << endl;
        else {
            if(ans == -1)
                cout << ans2 << endl;
            else if(ans2 == -1)
                cout << ans << endl;
            else
                cout << min(ans, ans2) << endl;
        }
    }
    return 0;
}
