#include <bits/stdc++.h>

using namespace std;

#define VI             vector <int>

bool tidy(int num)
{
    VI data;

    while (num)
    {
        data.push_back(num%10);
        num /= 10;
    }
    reverse(data.begin(), data.end());

    int len = data.size();

    if (len == 1)
        return true;

    for (int i=1; i<len; i++)
    {
        if (data[i] < data[i-1])
            return false;
    }
    return true;
}

int main()
{
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int tc, tcase=1;
    cin >> tc;

    while (tc--)
    {
        int num;
        cin >> num;

        while (!tidy(num))
        {
            num -= 1;
        }
        cout << "Case #" << tcase++ << ": " << num << endl;
    }
    return 0;
}
