#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-small-attempt1.in","w",stdout);
    int t,cs=0;
    cin >> t;
    while (t--)
    {
        cs++;
        int k,ans1(0),ans2(0);
        string s,s1;
        cin >> s >> k;
        s1=s;
    //    cout << s <<" " << k<< endl;
        for (int i=0;i<s.size();i++)
        {
            if (s[i]=='-')
            {
                ans1++;
                int o=s.size();
                for (int j=min(o-k,i);j<min(i+k,o);j++)
                {
                    if (s[j]=='+')
                        s[j]='-';
                    else s[j]='+';
                }
            }
            //cout << s << endl;
        }
        bool ok=false;
        for (int i=s.size()-1;i>=0;i--)
        {
            if (s[i]=='-')
            {
                ok=true;
                break;
            }
        }
        if (ok)
        {
            cout << "Case #"<<cs<<": IMPOSSIBLE\n";
        }
        else
            cout << "Case #"<<cs << ": "<<ans1 << "\n";
    }
    return 0;
}
