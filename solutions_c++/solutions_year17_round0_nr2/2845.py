#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;

int t;

int main()
{
    ifstream cin("B-large.in");
    ofstream cout("Bout.out");
    ios_base::sync_with_stdio(false), cin.tie(nullptr);

    cin >> t;
    for (int num = 0; num < t; num++)
    {
        string s, ans;
        cin >> s;

        for (int i = 0; i < (int)s.size(); i++)
        {
            if (!i || s[i] >= s[i - 1])
                ans += s[i];
            else
            {
                int it = i - 1;
                while (it >= 0 && ((s[it] == '0' || s[it] == '1') || (it && s[it] == s[it - 1])))
                {
                    ans.pop_back();
                    it--;
                }

                if (it >= 0)
                {
                    char c = s[it];
                    ans.pop_back();
                    ans += (--c);
                    for (int j = it + 1; j < (int)s.size(); j++)
                        ans += '9';
                }
                else
                    for (int j = 0; j < (int)s.size() - 1; j++)
                        ans += '9';
                break;
            }
        }

        cout << "case #" << num + 1 << ": " << ans << endl;
    }
    return 0;
}
