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
        long long n;
        cin >> n;
        vector< int > ans;
        int prev = 9;
        while(n)
        {
            int current = n%10;
            if(current>prev)
            {
                current--;
                for(int& i : ans)
                    i=9;
            }
            ans.push_back(current);
            prev = current;
            n/=10;
        }
        reverse(ans.begin(), ans.end());
        cout << "Case #" << tc << ": ";
        if(ans[0] == 0)
            ans.erase(ans.begin());
        for(int i : ans)
            cout << i;
        cout << endl;
    }

    return 0;
}
