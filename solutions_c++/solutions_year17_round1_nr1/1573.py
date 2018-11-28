#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n, m;
        cin >> n >> m;
        vector<string> a(n);
        for (int j = 0; j < n; ++j)
            cin >> a[j];
        for (int j = 0; j < n; ++j)
        {
            for (int k = 0; k < m; ++k)
            {
                if (a[j][k] == '?')
                {
                    if (k != 0)
                        a[j][k] = a[j][k - 1];
                }
                int p = 0;
                while (p < m && a[j][p] == '?')
                    ++p;
                if (p < m && a[j][p] != '?')
                    for (int l = 0; l < p; ++l)
                        a[j][l] = a[j][p];

            }
        }
        for (int j = 0; j < n; ++j)
        {
            for (int k = 0; k < m; ++k)
            {
                if (a[j][k] == '?')
                {
                    if (j != 0)
                        a[j][k] = a[j - 1][k];
                }
            }
        }
        string pyt(m, '?');
        int p = 0;
        while (p < n && a[p] == pyt)
            ++p;
        for (int j = 0; j < p; ++j)
            a[j] = a[p];
        cout << "Case #" << i + 1 << ":" << endl;
        for (int j = 0; j < n; ++j)
            cout << a[j] << endl;
    }
    return 0;
}
