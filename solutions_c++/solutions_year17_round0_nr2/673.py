#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

void work0(string st)
{
    bool flag = true;
    size_t pos = 0;
    for (size_t i = 1; i < st.size(); ++i)
    {
        if (st[i] < st[i - 1])
        {
            flag = false;
            break;
        }
        if (st[i] > st[i - 1]) pos = i;
    }
    if (flag)
    {
        cout << st << endl;
    }
    else
    {
        --st[pos];
        for (size_t i = pos + 1; i < st.size(); ++i) st[i] = '9';
        if (st[0] != '0') cout << st[0];
        for (size_t i = 1; i < st.size(); ++i) cout << st[i];
        cout << endl;
    }
}

void work(int n)
{
    for (int _ = 1; _ <= n; ++_)
    {
        printf("Case #%d: ", _);
        string st;
        cin >> st;
        work0(st);
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    work(n);
    return 0;
}
