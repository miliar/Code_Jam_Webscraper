#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
void flip(string &cake, int pos, int size)
{
    for (int i = pos; i < pos + size; ++i)
    {
        if (cake[i] == '-')
            cake[i] = '+';
        else
            cake[i] = '-';
    }
}
void functions()
{
    string pan;
    int s, times = 0;
    cin >> pan >> s;
    if (pan.length() < s)
    {
        for (int i = 0; i < pan.length(); ++i)
        {
            if (pan[i] == '-')
            {
                cout << "IMPOSSIBLE\n";
                return;
            }
        }
        cout << 0 << endl;
    }
    else if (pan.length() == s)
    {
        for (int i = 0; i < s; ++i)
        {
            if (pan[i] == '+')
            {
                ++times;
            }
            else 
            {
                --times;
            }
        }
        if (times == s)
        {
            cout << 0 << endl;
        }
        else if (-times == s)
        {
            cout << 1 << endl;
        }
        else
        {
            cout << "IMPOSSIBLE\n";
        }
        return;
    }
    else if (pan.length() > s)
    {
     //   cout << "here\n";
        for (int i = 0; i < pan.length() - s + 1; ++i)
        {
            if (pan[i] == '-')
            {
                flip(pan, i, s);
                ++times;
            }
       //     cout << pan << endl;
        }
        for (int i = pan.length() - s; i < pan.length(); ++i)
        {
            if (pan[i] == '-')
            {
                cout << "IMPOSSIBLE\n";
                return;
            }
        }
        cout << times << endl;
        return;
    }
}
int main()
{
    int n;
    cin >> n;
    for (int i = 1; i < n + 1; ++i)
    {
        cout << "Case #" << i << ": ";
        functions();
    }
}