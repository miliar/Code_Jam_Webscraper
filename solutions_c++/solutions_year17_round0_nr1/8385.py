#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

bool ok(string str)
{
    return str.find('-') == string::npos;
}

void flip(string& str, int k, int start)
{
    while (k--)
    {
        str[start + k] = (str[start + k] == '+') ? '-' : '+';
    }
}

int main()
{
    int T;
    cin >> T;
    int t = 0;
    while (++t <= T)
    {
        string str;
        int k;
        cin >> str >> k;
        int ans = 0;
        set<string> st;
        queue<string> q;
        queue<int> num;
        q.push(str);
        num.push(1);
        st.insert(str);
        bool success = false;
        while (!q.empty())
        {
            int n = num.front();
            num.pop();
            int sum = 0;
            bool found = false;
            while (n--)
            {
                string temp = q.front();
                q.pop();
                if (ok(temp))
                {
                    found = true;
                    break;
                }
                for (int i = 0;i <= temp.length() - k;i++)
                {
                    string s = temp;
                    flip(s, k, i);
                    if (st.count(s) != 0)
                    {
                        continue;
                    }
                    q.push(s);
                    st.insert(s);
                    sum++;
                }
            }
            if (found)
            {
                success = true;
                break;
            }
            else
            {
                ans++;
                num.push(sum);
            }
        }
        cout << "Case #" << t << ": ";
        if (!success)
        {
            cout << "IMPOSSIBLE";
        }
        else
        {
            cout << ans;
        }
        cout << endl;
    }
}