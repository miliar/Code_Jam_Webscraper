#include <iostream>
#include <string>

using namespace std;

class  Solution
{
public:
    string FlipPancake(string s, int k)
    {
        int res = 0, n = s.length();
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '+') continue;
            if (n - i < k)
            {
                res = -1;
                break;
            }
            res++;
            for (int j = i; j < i + k; j++)
            {
                if (s[j] == '-')
                {
                    s[j] = '+';
                }
                else
                {
                    s[j] = '-';
                }
            }
        }
        return res == -1 ? "IMPOSSIBLE" : to_string(res);
    }

};

void main() {
    int t;
    string s;
    int k;
    cin >> t;
    Solution sol;
    for (int i = 1; i <= t; ++i) {
        cin >> s >> k;
        cout << "Case #" << i << ": " << sol.FlipPancake(s, k) << endl;
    }
}