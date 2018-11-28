#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

char str[1001];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        int K;
        scanf(" %s %d", str, &K);
        int len = strlen(str);
        int ans = 0;
        for (int i = 0; i <= len - K; i ++)
        {
//            cout<<str<<endl;
            if (str[i] == '+') continue;
            ans++;
            for (int j = 0; j < K; j++)
            {
                if (str[i + j] == '+') str[i + j] = '-';
                else                   str[i + j] = '+';
            }
        }
        printf("Case #%d: ", cas);
        bool flag = false;
        for (int i = len - K + 1; i < len; i++)
            if (str[i] == '-') {flag = true; break;}
        if (!flag) printf("%d\n", ans);
        else       puts("IMPOSSIBLE");
    }
    return 0;
}
