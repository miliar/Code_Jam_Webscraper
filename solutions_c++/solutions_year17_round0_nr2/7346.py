#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    string N;
    for (int i = 0; i < T; ++i) {
        cin >> N;
        char num = N[0];
        string ans;
        long long int idx = 0;
        long long int j;
        for (j = 1; j < N.size(); ++j) {
            if (num < N[j]) {
                num = N[j];
                idx = j;
            } else if (num > N[j]) break;
        }
        if (j == N.size()) ans = N;
        else if (idx == 0 && j < N.size() && N[0] == '1') ans = string(N.size() - 1, '9');
        else {
            copy(N.begin(), N.begin() + idx, ans.begin());
            ans += N.substr(0, idx);
            ans += N[idx] - 1;
            ans += string(N.size() - idx - 1, '9');
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }

    return 0;
}
