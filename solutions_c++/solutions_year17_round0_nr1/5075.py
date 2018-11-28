#include <bits/stdc++.h>
#define optimezeio ios_base::sync_with_stdio(0);cin.tie

using namespace std;

int main () {
    optimezeio(0);
    int n = 0;
    bool flag = false;

    cin >> n;

    for (int l = 1; l <= n; ++l)
    {
        string s = "";
        int k = 0;
        int movs = 0;

        cin >> s >> k;

        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '-') {
                if (i + k > s.size()) {
                    flag = true;
                    break;
                }


                int j = 0;
                movs++;
                for (int j = 0; j < k; ++j)
                {
                    if (s[i + j] == '-')
                    {
                        s[i + j] = '+';
                    } else {
                        s[i + j] = '-';
                    }
                }
            }
        }

        if (flag) {
            cout << "Case #" << l << ": " << "IMPOSSIBLE" << endl;
            flag = false;
        } else {
            cout << "Case #" << l << ": " << movs << endl;
        }
    }

    return 0;
}