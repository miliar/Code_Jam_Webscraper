#include <bits/stdc++.h>

#define mp make_pair

typedef std::pair<int, int> pii;

void get_ans(std::string s)
{
    int last = 0;
    int yk = 0;
    int len = s.length();
    while (yk < len - 1 && s[yk] <= s[yk + 1])
    {
        if (s[yk] < s[yk + 1])
            last = yk + 1;
        ++yk;
    }
    if (yk == len - 1)
        std::cout << s << "\n";
    else
    {
        for (int i = 0; i < last; ++i)
            std::cout << s[i];
        if (s[last] > '1' || last > 0)
            std::cout << (char)(s[last] - 1);
        for (int i = last + 1; i < len; ++i)
            std::cout << '9';
         std::cout << "\n";
    }
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int n;
    scanf("%d", &n);
    n = 0;
    std::string s;
    while (std::cin >> s)
    {
        printf("Case #%d: ", ++n);
        get_ans(s);
    }
    return 0;
}