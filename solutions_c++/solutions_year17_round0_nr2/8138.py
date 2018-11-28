#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-small-attempt1.in","w",stdout);
    int t,cs=0;
    cin >> t;
    while (t--)
    {
        cs++;
        string s;
        cin >> s;
        //cout << s << endl;
        int l(0),r(s.size()-1);
        for (int i=r;i>l;i--)
        {
            if (s[i]<s[i-1] || s[i]=='0')
            {
                s[i-1]--;
                for (int j=i;j<=r;j++)
                    s[j]='9';
            }
        }
        if (s[l]=='0')
            l++;
        cout << "Case #" << cs << ": ";
        for (int i=l;i<=r;i++)
            cout<< s[i];
        cout << "\n";
    }
    return 0;
}
