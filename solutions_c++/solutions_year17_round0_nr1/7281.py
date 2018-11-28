#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

string IMPOSSIBLE = "IMPOSSIBLE";

void invert(char& c)
{
    if (c == '-')
    {
        c = '+';
    }
    else if (c == '+')
    {
        c = '-';
    }
}

void solution()
{
    string s;
    cin >> s;
    int len;
    cin >> len;
    int ans = 0;
    for (int i = 0; i < s.size(); ++i)
    {
        if (i + len > s.size())
        {
            break;
        }
        
        if (s[i] == '-')
        {
            ans++;
            for (int j = 0; j < len; ++j)
            {
                invert(s[i+j]);
            }
        }
    }
    
    for (int i = 0; i < s.size(); ++i)
    {
        if (s[i] == '-')
        {
            cout << "IMPOSSIBLE";
            return;
        }
    }

    cout << ans;
}

int main(int argc, char *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        stringstream ss;
        ss << (i+1);
        cout << "Case #" << ss.str() << ": ";
        solution();
        cout << "\n";
    }

    return 0;
}
 