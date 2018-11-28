#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<int> l, to, p, k;
int emp = 0;

void add(int pos, int z)
{
    if (emp == 0)
    {
        emp = 1;
        k[z]--;
        l[0] = z;
    }
    l[emp] = z;
    p[emp] = pos;
    to[emp] = to[pos];
    p[to[pos]] = emp;
    to[pos] = emp;
    emp++;
}

bool fnd (int c)
{
    if (emp == 0)
    {
        add(0, c);
        return true;
    }
    int v = 0;
    for (int i = 0; i < emp; i++)
    {
        if (l[v] != c && l[to[v]] != c)
        {
            add(v, c);
            k[c]--;
            return true;
        }
        else
            v = to[v];
    }
    return false;
}

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t, i, j, n;
    cin >> t;
    for (i = 0; i < t; i++)
    {
        bool check = true;
        int cnt;
        cin >> n;
        emp = 0;
        l.resize(n+100);
        to.resize(n+100);
        p.resize(n+100);
        int mx = 0;
        for (j = 0; j < 6; j++)
        {
            cin >> cnt;
            if (!(j&1))
                k.push_back(cnt);
            if (cnt > k[mx])
                mx = j/2;
        }
        if (n - k[mx] >= k[mx])
        {
            for (j = 0; j < k[mx]; j++)
                add(j, mx);
            int cur;
            for (cur = 0; cur < 3; cur++)
                if (k[cur] != 0 && cur != mx)
                    break;
            for (j = k[mx]; j >= 0; j--)
            {
                if (k[cur] == 0)
                    for (cur; cur < 3; cur++)
                        if (k[cur] != 0 && cur != mx)
                            break;
                add(j, cur);
                k[cur]--;
            }
            k[mx] = 0;
            for (j = 0; j < 3; j++, j %= 3)
            {
                if (k[0] == 0 && k[1] == 0 && k[2] == 0)
                    break;
                if (k[j] != 0 && !fnd(j))
                {
                    check = false;
                    break;
                }
            }
        }
        else
            check = false;
        cout << "Case #" << i+1 << ": ";
        if (!check)
            cout << "IMPOSSIBLE";
        else
        {
            int v = 0;
            for (j = 0; j < n; j++)
            {
                if (l[v] == 0)
                    cout << "R";
                if (l[v] == 1)
                    cout << "Y";
                if (l[v] == 2)
                    cout << "B";
                v = to[v];
            }
        }
        cout << endl;
        l.clear();
        to.clear();
        p.clear();
        k.clear();
    }
    return 0;
}
