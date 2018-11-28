#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1123456;
const int mod = 1e9 + 7;
const int inf = 1e9 + 7;
int read()
{
    int x;
    scanf("%I64d", &x);
    return x;
}
int a[12345];
int b[12345];
main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int n, m, i, j;
    cin >> n;
    string s;
    for(i = 1; i <= n; i ++)
    {
        cin >> s;
        cin >> m;
        int cnt = 0;
        for(j = 0; j < s.size(); j ++)
        {
            b[j] = 0;
            a[j] = (s[j] == '+');
        }
        int t = 0;
        for(j = 0; j < s.size(); j ++)
        {
            t ^= b[j];
            if(!(t ^ a[j]))
            {
                cnt ++;
                b[j + m] ^= 1;
                t ^= 1;
            }
            if(j + m == s.size())
            {
                bool ok = 1;
                for(int h = j + 1; h < s.size(); h ++)
                {
                    t ^= b[h];
                    if(!(t ^ a[h]))
                        ok = 0;
                }
                if(ok)
                    cout << "Case #" << i << ": " << cnt << endl;
                else
                    cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
                break;
            }
        }
    }
}

