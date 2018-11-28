#include <iostream>
#include <cstring> 
using namespace std;

int T;

int main()
{
    char s[20];
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> s;
        cout << "Case #" << t << ": ";
        int l = strlen(s);
        int pos;
        for (pos = 0; pos < l; ++pos)
            if (pos && s[pos - 1] > s[pos])
                break;
        if (pos < l)
        {
            --pos;
            while (pos && s[pos] - 1 < s[pos - 1]) --pos;
            --s[pos++];
            for (; pos < l; ++pos) s[pos] = '9';
        }
        for (pos = 0; s[pos] == '0' && pos < l; ++pos);
        for (; pos < l; ++pos) cout << s[pos];
        cout << endl;
    }

    return 0;
}
