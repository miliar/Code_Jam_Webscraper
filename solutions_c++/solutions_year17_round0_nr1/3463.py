#include <iostream>
using namespace std;

int main()
{
    int t;
    string s;
    cin >> t;
    for (int m=1;m<=t;++m)
    {
        cin >> s;
        int k,cnt=0;
        cin >> k;
        for (int i=0;i+k<=s.length();++i)
        {
            if (s[i]=='-')
            {
                for (int j=i;j<i+k;++j)
                    if (s[j]=='+') s[j] = '-';
                    else s[j] = '+';
                ++cnt;
            }
        }
        bool yes = true;
        for (int i=s.length()-k+1;i<s.length();++i)
            if (s[i]=='-')
            {
                yes = false;
                break;
            }
        if (yes) cout << "Case #" << m << ": " << cnt << endl;
        else cout << "Case #" << m << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
