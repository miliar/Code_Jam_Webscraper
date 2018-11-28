#include <bits/stdc++.h>
using namespace std;


int main() {
    #ifdef LOCAL
        freopen("z.in", "rt", stdin);
        freopen("z.out", "wt", stdout);
    #endif

    int t, k;
    string p;
    cin >> t;
    for(int test = 1; test <= t; test++)
    {
        cin >> p >> k;
        cout << "Case #" << test << ": ";
        int res = 0;
        for(int i = 0; i <= p.length()-k; i++)
        {
            if(p[i] == '-')
            {
                res++;
                for(int j = 0; j < k; j++)
                {
                    if(p[i+j] == '-')
                        p[i+j] = '+';
                    else
                        p[i+j] = '-';
                }
            }
        }
        for(int i = 0; i < p.length(); i++)
        {
            if(p[i] == '-') {
                res = -1;
                break;
            }
        }
        if(res >= 0)
            cout << res << '\n';
        else
            cout << "IMPOSSIBLE\n";
    }
    cerr << "done";
    return 0;
}