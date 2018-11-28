#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string s;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t, i, j, p, k;
    cin >> t;
    for (i = 0; i < t; i++)
    {
        int ans = 0;
        cin >> s >> k;
        int l = s.length();
        bool check = true;
        for (j = 0; j < s.length(); j++)
            if (s[j] == '-')
            {
                if (l - j < k)
                {
                    check = false;
                    break;
                }
                ans++;
                for (int p = 0; p < k; p++)
                    if (s[j+p] == '+')
                        s[j+p] = '-';
                    else
                        s[j+p] = '+';
            }
        cout << "Case #" << i+1 << ": ";
        if (check)
            cout << ans;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
