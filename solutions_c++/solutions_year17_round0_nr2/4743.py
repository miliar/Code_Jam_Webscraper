#include <bits/stdc++.h>
using namespace std;
typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;

int main()
{
    freopen("in", "r", stdin);
    UI T;
    cin >> T;
    for (UI t = 1; t <= T; ++t) {
        string S;
        cin >> S;
        bool flag = false;
        for (int i = 0; i+1 < S.size(); ++i) {
            if (S[i] > S[i+1]) {
                for (int j = i+1; j < S.size(); ++j) {
                    S[j] = '0';
                }
                flag = true;
                int j = i;
                while (j > 0 && S[j] == S[j-1]) {
                    S[j] = '0';
                    --j;
                }
                break;
            }
        }
        istringstream iss(S);
        ULL ans = 0;
        iss >> ans;
        if (flag) --ans;
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

