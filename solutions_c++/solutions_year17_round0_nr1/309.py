#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int k;
        string s;
        cin >> s >> k;

        vector<int> a;
        for (int i = 0, j = 0; i + k <= s.size(); i++)
        {
            for (; j < a.size() && a[j] + k <= i; j++);
            if ((s[i] == '-') != (a.size() - j) % 2)
                a.push_back(i);
        }

        for (int i = s.size() - k + 1, j = 0; i < s.size(); i++)
        {
            for (; j < a.size() && a[j] + k <= i; j++);
            if ((s[i] == '-') != (a.size() - j) % 2)
            {
                k = 0;
                break;
            }
        }


        cout << "Case #" << tt << ": ";
        if (k)
            cout << a.size();
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }

    return 0;
}
