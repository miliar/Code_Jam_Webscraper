#include <bits/stdc++.h>

using namespace std;

string x;

void fill9(int ind)
{
    int i;
    for(i=ind;i<x.size();i++)
        x[i]='9';
}

string nolz(string s)
{
    int i;
    for(i=0;i<s.size();i++)
    {
        if(s[i]!='0')
            return s.substr(i);
    }
    return "0";
}

int main()
{
    freopen("B_large.in","r",stdin); freopen("B_large.out","w",stdout);
    int t;
    cin >> t;
    int tc;
    for(tc=1;tc<=t;tc++)
    {
        cin >> x;
        int i;
        for(i=1;i<x.size();i++)
        {
            if(x[i]<x[i-1])
            {
                fill9(i);
                x[i-1]--;
                i--;
                while(i>0&&x[i]<x[i-1])
                {
                    x[i]='9';
                    x[i-1]--;
                    i--;
                }
                break;
            }
        }
        x=nolz(x);
        cout << "Case #" << tc << ": " << x << endl;
    }
}
