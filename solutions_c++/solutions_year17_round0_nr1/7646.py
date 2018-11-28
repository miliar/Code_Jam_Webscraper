#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int i=1; i<=T; i++)
    {
        string s;
        int k;

        cin >> s >> k;

        int count = 0;
        for(int j=s.size()-1; j>=k-1; j--)
        {
            if(s[j] == '+')
                continue;
            else
            {
                for(int x=j; x>(j-k); x--)
                    s[x] = ((s[x] == '-') ? '+' : '-');
                count++;
            }
        }

        bool possible = true;
        for(int j=0; j<k && possible; j++)
        {
            if(s[j] == '-')
                possible = false;
        }

        cout << "Case #" << i << ": ";
        if(possible)
            cout << count << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}
