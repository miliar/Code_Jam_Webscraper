#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    cin >> N;
    cin.get();
    for (int t = 1; t<=N; t++)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;

        int ans = 0;
        while (true)
        {
            int i = 0;
            while (i < s.size() && s[i] == '+')
                i++;
            if (i >= s.size())
            {
                cout << "Case #" << t << ": " << ans << endl;
                break;
            }
            if (i + k > s.size())
            {
                cout << "Case #" << t << ": IMPOSSIBLE" << endl;
                break;
            }
            for (int j = i; j < i + k; j++)
            {
                s[j] = s[j] == '+' ? '-' : '+';
            }
            ans++;
        }

    }
    return 0;
}
