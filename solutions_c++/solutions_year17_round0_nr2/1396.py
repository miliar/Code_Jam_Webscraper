#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool bigger(string a, string b)
{
    return (a.size() > b.size() || (a.size() == b.size() && a > b));
}

string normal(string s)
{
    while (s.size() > 1 && s[0] == '0')
    {
        s.erase(s.begin());
    }
    return s;
}

bool good(string s)
{
    for (int i = 1; i < (int) s.size(); i++)
    {
        if (s[i] < s[i - 1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
#ifdef ONPC
    freopen("B-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string s;
        cin >> s;
        string ans = "0";
        for (int j = 0; j < (int) s.size(); j++)
        {
            if (j == 0)
            {
                string now = s;
                now[j]--;
                for (int k = j + 1; k < (int) now.size(); k++)
                {
                    now[k] = '9';
                }
                now = normal(now);
                if (bigger(now, ans))
                {
                    ans = now;
                }
            }
            else
            {
                if (s[j] == '0')
                {
                    if (s[j - 1] > s[j])
                    {
                        break;
                    }
                    continue;
                }
                else
                {
                    string now = s;
                    now[j]--;
                    for (int k = j + 1; k < (int) now.size(); k++)
                    {
                        now[k] = '9';
                    }
                    if (now[j - 1] > now[j])
                    {
                        if (s[j - 1] > s[j])
                        {
                            break;
                        }
                        continue;
                    }
                    now = normal(now);
                    if (bigger(now, ans))
                    {
                        ans = now;
                    }
                }
            }
            if (j && s[j] < s[j - 1])
            {
                break;
            }
        }
        if (good(s))
        {
            ans = s;
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
