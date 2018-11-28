#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

char t[N];

bool solve()
{
    int n, k, p = 0, m = 0;
    scanf("%s%d", t, &k);
    string s;
    n = strlen(t);
    s = t;
    for (int i = 0; i + k <= n; ++i)
        if (s[i] == '-') {
            p++;
            for (int j = i; j < i + k; ++j)
                s[j] = "+-"[s[j]=='+'];
        }
    if (s.find('-') != -1)
        p = inf;
   /* s = t;
    for (int i = 0; i + k <= n; ++i)
        if (s[i] == '+') {
            m++;
            for (int j = i; j < i + k; ++j)
                s[j] = "+-"[s[j]=='+'];
        }
    if (s.find('+') != -1)
        m = inf;*/
    int ans = p;
    if (ans == inf)
        puts("IMPOSSIBLE");
    else
        printf("%d\n", ans);
    return false;
}

int main()
{
        freopen("input.txt","r", stdin);
        freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
