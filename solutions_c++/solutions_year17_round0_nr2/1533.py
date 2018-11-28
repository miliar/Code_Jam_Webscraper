#include <iostream>
#include <cstring>
using namespace std;

bool sorted(string const& s)
{
    for (int i = 1; i < s.size(); ++i)
        if (s[i - 1] > s[i])
                return false;
    return true;
}

void print(string const& s)
{
    bool nonzero = false;
    for (char c : s)
    {
        if (c != '0')
        {
            nonzero = true;
            cout << c;
        }
        else if (nonzero)
            cout << c;

    }
    cout << endl;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas)
    {
        cout << "Case #" << cas << ": ";

        string s;
        cin >> s;
        
        if (sorted(s))
            cout << s << endl;
        else
        {
            for (int i = s.size() - 1; i >= 0; --i)
            {
                if (s[i] == '0') 
                    continue;

                string r = s;
                r[i] = s[i] - 1;
                for (int j = i + 1; j < s.size(); ++j)
                    r[j] = '9';
                if (sorted(r))
                {
                    print(r);
                    break;
                }
            }
        }
    }
}
