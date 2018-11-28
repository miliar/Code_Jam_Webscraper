#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
typedef unsigned long long ull;
using namespace std;

vector<int> intToDigits(ull n)
{
    vector<int> ans;
    while(n >= 10)
    {
        ans.push_back(n % 10);
        n /= 10;
    }
    ans.push_back(n);
    reverse(ans.begin(), ans.end());
    return ans;
}

ull genAns(int posToDecrease, vector<int> digits)
{
    ull ans = 0;
    if (posToDecrease == 0 && digits[0] == 1)
    {
        for (int i = 1; i < digits.size(); ++i)
            ans = ans * 10 + 9;
    }
    else
    {
        digits[posToDecrease]--;
        for (int p = posToDecrease + 1; p < digits.size(); ++p)
            digits[p] = 9;
        for (int p = 0; p < digits.size(); ++p)
            ans = ans * 10 + digits[p];
    }
    return ans;
}

ull solve(ull n)
{
    if (n < 10)
        return n;

    ull ans = 0;
    vector<int> digits = intToDigits(n);
    int posToDecrease = 0;
    bool nondecreasing = true;
    for(int pos = 0; pos < digits.size(); ++pos)
    {
        if (pos > 0 && digits[pos] > digits[pos - 1] && nondecreasing)
            posToDecrease = pos;
        if (pos > 0 && digits[pos] < digits[pos - 1])
            nondecreasing = false;
    }
    if (nondecreasing)
        return n;
    return genAns(posToDecrease, digits);
}

int main()
{
    ull n, t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> n;   
        cout <<  "Case #" << i + 1 << ": " << solve(n) << endl;
    }
}
