#include <bits/stdc++.h>
#define optimezeio ios_base::sync_with_stdio(0);cin.tie

using namespace std;

int main () {
    optimezeio(0);
    int n = 0;

    cin >> n;

    for (int l = 1; l <= n; ++l)
    {
        string s = "";
        cin >> s;
        if (s.size() == 1) {
            cout << "Case #" << l << ": " << s[0] << endl;
            continue;
        }

        int lastpos = s.size() - 1;

        for (int i = lastpos; i > 0; --i)
        {
            if (s[i - 1] <= s[i])
                continue;

            else {
                s[i - 1] = s[i - 1] - 1;

                for (int j = i; j < s.size(); ++j)
                {
                    s[j] = '9';
                }
            }
        }
        
        if (s[0] == '0') {
            cout << "Case #" << l << ": " << s.substr(1) << endl;
        } else
            cout << "Case #" << l << ": " << s << endl;
    }

    return 0;
}