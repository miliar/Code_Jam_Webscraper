#include <iostream>
#include <string>

using namespace std;

class  Solution
{
public:
    long long TidyNumbers(long long n)
    {
        string s = to_string(n);
        int i = 1;
        for (; i < s.length(); i++)
        {
            if (s[i] < s[i - 1]) break;
        }
        if (i == s.length()) return n;
        for (; i >= 1; i--)
        {
            if (s[i] > s[i - 1]) break;
        }
        long long res = stoll(s.substr(0, i + 1)) - 1;
        for (int j = 0; j < s.length() - i-1; j++)
        {
            res *= 10; 
            res += 9;
        }
        return res;
    }
};

void main() {
    int t;
    long long n;
    cin >> t;
    Solution sol;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": " << sol.TidyNumbers(n) << endl;
    }
}