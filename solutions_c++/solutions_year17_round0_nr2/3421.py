#include <iostream>
using namespace std;

int main()
{
    int t;
    string s;
    cin >> t;
    for (int m=1;m<=t;++m)
    {
        int id=0, j=1;
        cin >> s;
        while (j<s.length() && s[j-1]<=s[j])
        {
            if (s[j-1]<s[j]) id = j;
            ++j;
        }
        if (j==s.length())
        {
            cout << "Case #" << m << ": " << s << endl;
        }
        else
        {
            cout << "Case #" << m << ": ";
            if (id==0 && s[id]=='1')
            {
                for (int i=1;i<s.length();++i) cout << '9';
            }
            else
            {
                --s[id];
                for (int i=0;i<id;++i) cout << s[i];
                cout << s[id];
                for (int i=id+1;i<s.length();++i) cout << '9';
            }
            cout << endl;
        }
    }
    return 0;
}
