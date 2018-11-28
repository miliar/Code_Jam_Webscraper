#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

void num(string& ans)
{
    int i = 1;

    for (; i < ans.size(); ++i)
    {
        if (ans[i] < ans[i - 1])
            break;
    }

    if (i != ans.size())
    {
        for (int j = i; j < ans.size(); ++j)
        {
            ans[j] = '9';
        }

        int j = i - 1;

        for (; j > 0; --j)
        {
            if (ans[j] != '0')
            {
                --ans[j];

                if (ans[j - 1] > ans[j])
                    ans[j] = '9';
                else break;
            }
            else
            {
                ans[j] = '9';
            }
        }

        if (j == 0 && ans[0] != '0')
        {
            --ans[j];
        }
    }

    while (ans.front() == '0')
    {
        ans.erase(ans.begin());
    }
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        string ans;
        cin >> ans;

        num(ans);
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}