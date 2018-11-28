#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("read.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,k,c=0;
    string s;
    bool b=1;
    cin  >> t;
    for(int i = 0 ; i < t ; i++)
    {
        b=1;
        c=0;
        cin >> s >> k;
        for(int j = 0 ; j < s.size()-k+1;j++)
            if(s[j]=='-')
            {
                for(int l = j ; l < j+k ; l++)
                {
                    if(s[l]=='-')
                        s[l]='+';
                    else
                        s[l]='-';
                }
                c++;
            }
        for(int j = 0 ; j < s.size() ; j++)
            if(s[j]=='-')
                b=0;
        cout << "Case #" << i+1 << ": ";
        if(b)
            cout << c << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }

}
