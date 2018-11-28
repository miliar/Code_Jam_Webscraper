#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

void work0(string st, int k)
{
    size_t len = st.size();
    int ans = 0;
    for (size_t i = 0; i < len; ++i)
    {
        if (i + k > len) break;
        if (st[i] == '-')
        {
            ++ans;
            for (size_t j = i; j < i + k; ++j)
            {
                if (st[j] == '-') st[j] = '+'; else st[j] = '-';
            }
        }
    }
    bool flag = true;
    for (int i = 0; i < st.size(); ++i)
    {
        if (st[i] == '-')
        {
            flag = false;
            break;
        }
    }
    if (flag)
    {
        cout << ans << endl;
    }
    else
    {
        cout << "IMPOSSIBLE\n";
    }
}

void work(int n)
{
    for (int _ = 1; _ <= n; ++_)
    {
        printf("Case #%d: ", _);
        string st;
        int k;
        cin >> st >> k;
        work0(st, k);
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    scanf("%d", &n);
    work(n);
    return 0;
}
