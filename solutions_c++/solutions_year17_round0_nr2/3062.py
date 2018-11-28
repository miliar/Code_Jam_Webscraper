#include <iostream>
#include <string>
#include <sstream>
using namespace std;
typedef long long LL;
LL n;
int check(const string &s)
{
    for (int i = 1; i < s.length(); ++i)
        if (s[i] < s[i - 1])
            return i;
    return -1;
}
int main()
{
    int T;
    cin >> T;
    for (int Ti = 1; Ti <= T; ++Ti)
    {
        cin >> n;
        string s;
        stringstream ss;
        ss << n;
        s = ss.str();
        while (1)
        {
            int t = check(s);
            if (t == -1)
                break;
            for (int i = t; i < s.length(); ++i)
                s[i] = '0';
            stringstream ss2(s);
            ss2 >> n;
            n--;
            stringstream ss3;
            ss3 << n;
            s = ss3.str();
        }
        cout << "Case #" << Ti << ": " << s << endl;
    }
    return 0;
}
