#include <iostream>

using namespace std;

string Licz(string s)
{
    int n = s.size();
    string x = s;
    string odp = "";
    for (int i = 0; i < n; ++i)
    {
        for (char c = ((i == 0) ? '1' : '0'); c < s[i]; ++c)
        {
            x[i] = c;
            bool db = true;
            for (int j = 0; j < i; ++j)
                if (x[j] > x[j + 1])
                    db = false;
            if (db)
            {
                for (int j = i + 1; j < n; ++j)
                    x[j] = '9';
                if (odp == "" || (odp != "" && x > odp))
                    odp = x;
            }
        }
        x[i] = s[i];
    }
    bool db = true;
    for (int i = 0; i < n - 1; ++i)
        if (s[i] > s[i + 1])
            db = false;
    if (db)
        return s;
    return odp;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        string s;
        cin >> s;
        int n = s.size();
        string odp = Licz(s);
        if (odp == "")
        {
            string odp2(n - 1, '9');
            odp = odp2;
        }
        cout << "Case #" << i + 1 << ": " << odp << endl;
    }
    return 0;
}
