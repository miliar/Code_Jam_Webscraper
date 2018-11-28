#include <bits/stdc++.h>

using namespace std;

struct activity
{
    int l, r, p;
    bool operator<(const activity& a) const
    {
        return l < a.l;
    }
} a[210];

void solve()
{
    int ac, aj;
    cin >> ac >> aj;
    int n = ac + aj;
    for (int i = 0; i < ac; i++)
    {
        cin >> a[i].l >> a[i].r;
        a[i].p = 0;
    }
    for (int i = 0; i < aj; i++)
    {
        cin >> a[ac + i].l >> a[ac + i].r;
        a[ac + i].p = 1;
    }
    sort(a, a + n);

    a[n].l = a[0].l + 24*60;
    a[n].r = a[0].r + 24*60;
    a[n].p = a[0].p;

    int t = a[0].r;
    int p = a[0].p;
    int pt[2] = {0, 0};
    vector<int> P[2], B;
    int add = 0;
    for (int i = 1; i < n + 1; i++)
    {
        int len = a[i].r - a[i].l;
        int dif = a[i].l - t;
        pt[1 - a[i].p] += len;
        if (p == a[i].p)
            P[1 - p].push_back(dif);
        else
        {
            if (dif == 0)
                add++;
            else
                B.push_back(dif);
        }
        t = a[i].r;
        p = a[i].p;
    }
    /*
    cout <<"-------"<< endl;
    cout << pt[0] << " " << pt[1] << endl;
    cout << add << endl;
    for (int i: P[0]) cout << i << " "; cout << endl;
    for (int i: P[1]) cout << i << " "; cout << endl;
    for (int i: B) cout << i << " "; cout << endl;
    cout <<"-------"<< endl;
    */
    vector<int> x(750, -1);
    x[pt[0]] = add;
    for (int len: P[0])
    {
        vector<int> y(750, -1);
        for (int i = 0; i <= 720; i++)
            if (x[i] != -1)
            {
                if (i + len <= 720)
                    if (y[i + len] == -1)
                        y[i + len] = x[i];
                    else
                        y[i + len] = min(y[i + len], x[i]);
                for (int j = 0; j < len && i + j <= 720; j++)
                    if (y[i + j] == -1)
                        y[i + j] = x[i] + 2;
                    else
                        y[i + j] = min(y[i + j], x[i] + 2);
            }
        x = y; 
        /*for (int i = 0; i <= 720; i++)
            if (x[i] != -1)
                cout << "(" << i <<"="<<x[i]<<") ";
        cout << endl;*/
    }
    for (int len: P[1])
    {
        vector<int> y(750, -1);
        for (int i = 0; i <= 720; i++)
            if (x[i] != -1)
            {
                if (y[i] == -1)
                    y[i] = x[i];
                else
                    y[i] = min(y[i], x[i]);
                for (int j = 1; j <= len && i + j <= 720; j++)
                    if (y[i + j] == -1)
                        y[i + j] = x[i] + 2;
                    else
                        y[i + j] = min(y[i + j], x[i] + 2);
            }
        x = y;
        /*for (int i = 0; i <= 720; i++)
            if (x[i] != -1)
                cout << "(" << i <<"="<<x[i]<<") ";
        cout << endl;*/
    }
    for (int len: B)
    {
        vector<int> y(750, -1);
        for (int i = 0; i <= 720; i++)
            if (x[i] != -1)
                for (int j = 0; j <= len && i + j <= 720; j++)
                    if (y[i + j] == -1)
                        y[i + j] = x[i] + 1;
                    else
                        y[i + j] = min(y[i + j], x[i] + 1);
        x = y;
        /*for (int i = 0; i <= 720; i++)
            if (x[i] != -1)
                cout << "(" << i <<"="<<x[i]<<") ";
        cout << endl;*/
    }
    cout << x[720] << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
