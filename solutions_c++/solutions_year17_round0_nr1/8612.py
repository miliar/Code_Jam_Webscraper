#include <bits/stdc++.h>

using namespace std;

int main()
{
    #ifdef FILEIO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);

    int tcn;
    cin >> tcn;
    for(int tc=1; tc<=tcn; tc++)
    {
        string str;
        int k;
        cin >> str >> k;
        int ans = 0;
        for(int i=0; i<str.size()-k+1; i++)
            if(str[i]=='-')
            {
                ans++;
                for(int j=i; j<i+k; j++)
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
            }
        cout << "Case #" << tc << ": ";
        bool possible = true;
        for(char& c : str)
            if(c != '+')
            {
                cout << "IMPOSSIBLE" << endl;
                possible = false;
                break;
            }
        if(possible)
            cout << ans << endl;
    }

    return 0;
}
