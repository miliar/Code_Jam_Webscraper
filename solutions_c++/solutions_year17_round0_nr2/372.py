#include <iostream>
#include <string>
#include <algorithm>
#define MAX_T 100
#define MAX_N_LENGTH 19
using namespace std;

string s;

void init()
{
    getline(cin, s);
}

void solve()
{
    int allNinePos = s.length();
    for (int i = s.length() - 1; i >= 1; i--)
    {
        if (s[i] < s[i-1])
        {
            s[i-1] = s[i-1] - 1;
            allNinePos = i;
        }
    }
    int nonZero;
    for (nonZero = 0; nonZero <= allNinePos - 1; nonZero++)
    {
        if (s[nonZero] != '0')
            break;
    }
    for (int i = nonZero; i <= allNinePos - 1; i++)
        cout << s[i];
    for (unsigned int i = allNinePos; i < s.length(); i++)
        cout << 9;
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
    }
    return 0;
}
