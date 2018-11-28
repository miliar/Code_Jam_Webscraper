#include <iostream>

using namespace std;

int Licz(string s, int k)
{
    int n = s.size();
    int il = 0;
    for (int i = 0; i <= n - k; ++i)
    {
        if (s[i] == '-')
        {
            ++il;
            for (int j = i; j <= i + k - 1; ++j)
            {
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            }
        }
    }
    bool db = true;
    for (int i = 0; i < n; ++i)
        if (s[i] == '-')
            return -1;
    return il;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        string s;
        int k;
        cin >> s >> k;
        int odp = Licz(s, k);
        cout << "Case #" << i + 1 << ": ";
        if (odp != -1)
            cout << odp << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
