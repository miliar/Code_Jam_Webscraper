#include <iostream>
#include <algorithm>
#include <limits>
#include <queue>
#include <string>

using namespace std;

void doCase()
{
    int64_t N;
    cin >> N;
    vector<int> digits;
    while(N>0)
    {
        int64_t digit = (N % int64_t(10));
        digits.push_back(digit);
        N /= int64_t(10);
    }
    for(int i=1; i<digits.size(); i++)
    {
        if(digits[i] > digits[i-1])
        {
            digits[i]--;
            for(int j=0; j<i; j++)
                digits[j] = 9;
        }
    }
    int64_t result = 0;
    for(int i=0; i<digits.size(); i++)
    {
        result *= int64_t(10);
        result += int64_t(digits[digits.size()-1-i]);
    }
    cout << result << endl;
}

int main()
{
    int T;
    cin >> T;
    for(int i=0; i<T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        doCase();
    }
}
