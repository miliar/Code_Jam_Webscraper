#include <iostream>
#include <string>

using namespace std;

string s;

void flip(int pos,int k)
{
    for (int i=pos;i<pos+k;i++)
    {
        if (s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,k;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        cout << "Case #" << i+1 << ": ";
        int wyn=0;
        cin >> s >> k;
        for (int j=0;j<=s.length()-k;j++)
        {
            if (s[j]=='-')
            {
                wyn++;
                flip(j,k);
            }
            //cerr << s << "\n";
        }
        bool ispos=true;
        for (int j=s.length()-k+1;j<s.length();j++)
        {
            if (s[j]=='-')
            {
                ispos=false;
                cout << "IMPOSSIBLE\n";
                break;
            }
        }
        if (ispos)
            cout << wyn << "\n";
    }
    return 0;
}
