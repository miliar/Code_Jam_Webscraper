#include <bits/stdc++.h>

#define mp make_pair

typedef std::pair<int, int> pii;

void get_ans(int n, int p)
{
    int r[n];
    for (int i = 0; i < n; ++i)
        scanf("%d", &r[i]);
    std::vector<int> q[n];
    int qle[n][p], qr[n][p];
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < p; ++j)
        {
            int a;
            scanf("%d", &a);
            q[i].push_back(a);
        }
        std::sort(q[i].begin(), q[i].end());
        for (int j = 0; j < p; ++j)
        {
            qr[i][j] = 10 * q[i][j] / 9 / r[i];
            qle[i][j] = 10 * q[i][j] / 11 / r[i];
            if (10 * q[i][j] > 11 * r[i] * qle[i][j])
                ++qle[i][j];    
        }
    }
    std::set<pii> st_ma, st_mi;
    int yk[n];
    for (int i = 0; i < n; ++i)
        yk[i] = p - 1;
    for (int i = 0; i < n; ++i)
    {
        st_ma.insert(std::mp(qr[i][p - 1], i));
        st_mi.insert(std::mp(qle[i][p - 1], i));
    }
    int not_bad = 1;
    int ans = 0;
    while (not_bad)
    {
        if ((*(--st_mi.end())).first <= (*st_ma.begin()).first)
        {
            ++ans;
            for (int i = 0; i < n; ++i)
            {
                st_ma.erase(std::mp(qr[i][yk[i]], i));
                st_mi.erase(std::mp(qle[i][yk[i]], i));
                --yk[i];
                if (yk[i] >= 0)
                {
                    st_ma.insert(std::mp(qr[i][yk[i]], i));
                    st_mi.insert(std::mp(qle[i][yk[i]], i));
                }
                else
                    not_bad = 0;
            }
        }
        else
        {   
            int num = (*(--st_mi.end())).second;
            st_ma.erase(std::mp(qr[num][yk[num]], num));
            st_mi.erase(std::mp(qle[num][yk[num]], num));
            --yk[num];
            if (yk[num] >= 0)
            {
                st_ma.insert(std::mp(qr[num][yk[num]], num));
                st_mi.insert(std::mp(qle[num][yk[num]], num));
            }
            else
                not_bad = 0;            
        }
    }
    printf("%d\n", ans);
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int ch;
    scanf("%d", &ch);
    ch = 0;
    int n, p;
    while (scanf("%d %d", &n, &p) == 2)
    {
        printf("Case #%d: ", ++ch);
        get_ans(n, p);
    }
    return 0;
}