#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        string s;
        int K;
        cin >> s >> K;

        int n = s.length();
        int res = 0;
        for(int i = 0; i <= n - K; i++)
        {
            if(s[i] == '+') continue;
            res++;
            for(int j = 0; j < K; j++)
            {
                if(s[i + j] == '+') s[i + j] = '-';
                else s[i + j] = '+';
            }
        }

        bool done = true;
        for(int i = 0; i < n; i++)
        {
            if(s[i] == '-') done = false;
        }

        cout << "Case #" << t << ": ";
        if(done) cout << res << endl;
        else cout << "IMPOSSIBLE" << endl;
    }


    return 0;
}