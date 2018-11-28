#include <iostream>
using namespace std;

// Returns true if digits of n are sorted in decreasing
// order
bool areSorted(unsigned long long int n)
{
    // Note that digits are traversed from last to first
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}

int main()
{
    int t;
    cin>>t;
    for (int i = 1; i <= t; ++i)
    {
    unsigned long long int n;
    cin>>n;
    while(n>0)
    {
        if(areSorted(n))
        {
            cout << "Case #" << i << ": " << n << endl;
            n--;
            break;
        }
        else
            n--;
    }
    }
    return 0;
}