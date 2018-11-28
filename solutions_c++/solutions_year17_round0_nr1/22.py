#include <bits/stdc++.h>
using namespace std;
int T, P, n, k;
string st;
int main()
{
    cin >> T;
    while (P ++, T --)
    {
        cin >> st; cin >> k;
        int n = st.length();
        int cnt = 0;
        for (int i = 0; i < n - k + 1; ++ i)
            if (st[i] == '-')
            {
                cnt ++;
                for (int j = i; j < i + k; ++ j)
                    if (st[j] == '+') st[j] = '-';
                    else st[j] = '+';
            }

        for (int i = 0; i < n; ++ i) if (st[i] == '-') cnt = -1;
            cout << "Case #" << P << ": ";
        if (cnt == -1) cout << "IMPOSSIBLE\n";
        else cout << cnt << "\n";

    }
}
