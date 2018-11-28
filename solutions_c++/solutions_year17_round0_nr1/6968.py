#include <bits/stdc++.h>

using namespace std;

bitset<1005> val;

int main()
{
    freopen("codejam/A-large.in", "r", stdin);
    freopen("codejam/A-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        printf("Case #%d: ", nc);
        string s;
        cin >> s;
        int k;
        scanf("%d", &k);
        val.set();
        for (int i = 0; i < s.size(); i++)
            val[i] = (s[i] == '+') ? 1 : 0;
        int res = 0;
        for (int i = 0; i <= s.size() - k; i++) {
            if (!val[i]) {
                res++;
                for (int j = i; j < i + k; j++) {
                    val.flip(j);
                }
            }
        }
        if (val.all())
            printf("%d\n", res);
        else
            printf("IMPOSSIBLE\n");
    }
}