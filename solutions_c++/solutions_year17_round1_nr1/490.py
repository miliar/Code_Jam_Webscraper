#include <bits/stdc++.h>

#define mp make_pair

typedef std::pair<int, int> pii;

void get_ans(int h, int w)
{
    int field[h][w];
    for (int i = 0; i < h; ++i)
    {
        std::string s;
        std::cin >> s;
        for (int j = 0; j < w; ++j)
            if (s[j] == '?')
                field[i][j] = -1;
            else
                field[i][j] = s[j] - 'a';
    }
    int prev_no_zero = -1;
    for (int i = 0; i < h; ++i)
    {
        int b = 1;
        for (int j = 0; j < w; ++j)
            b = b && field[i][j] == -1;
        if (!b)
        {
            int yk = 0;
            while (field[i][yk] == -1)
                ++yk;
            int ne_char = field[i][yk];
            for (int j = 0; j < w; ++j)
            {
                if (field[i][j] != -1)
                    ne_char = field[i][j];
                field[i][j] = ne_char;
            }
            for (int k = prev_no_zero + 1; k < i; ++k)
                for (int j = 0; j < w; ++j)
                    field[k][j] = field[i][j];
            prev_no_zero = i;
        }    
    }
    for (int k = prev_no_zero + 1; k < h; ++k)
        for (int j = 0; j < w; ++j)
            field[k][j] = field[prev_no_zero][j];
    for (int i = 0; i < h; ++i)
    {
        for (int j = 0; j < w; ++j)
            printf("%c", field[i][j] + 'a');
        printf("\n");
    }
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int ch;
    scanf("%d", &ch);
    ch = 0;
    int n, m;
    while (scanf("%d %d", &n, &m) == 2)
    {
        printf("Case #%d:\n", ++ch);
        get_ans(n, m);
    }
    return 0;
}