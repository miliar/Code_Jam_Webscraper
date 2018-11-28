#include <iostream>
#include <string>
#include <algorithm>
#define MAX_K 1000
using namespace std;

int k;
int length;
bool s[MAX_K];

void init()
{
    length = 0;
    char ch;
    while ((ch = getchar()) != ' ')
    {
        if (ch == '-')
            s[length] = false;
        else
            s[length]=true;
        length++;
    }
    cin >> k;
}
bool check()
{
    for (int i = length - k + 1; i < length; i++)
        if (s[i] == false)
            return false;
    return true;
}
void solve()
{
    int steps = 0;
    for (int i = 0; i < length - k + 1; i++)
        if (s[i] == false)
        {
            steps++;
            for (int j = i; j <= i + k - 1; j++)
                s[j] = !s[j];
        }

    if (check())
        cout << steps;
    else
        cout << "IMPOSSIBLE";
}

int main()
{
    int t;
    string s;
    cin >> t;
    getline(cin, s);
    for (int i = 1; i <= t; i++)
    {
        init();
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
        getline(cin, s);
    }
    return 0;
}
