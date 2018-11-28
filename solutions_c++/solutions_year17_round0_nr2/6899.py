#include <iostream>
#include <cmath>
using namespace std;

// get index of the digit that is not sorted
int index(int64_t n)
{
    // want to return first digit from left side
    string number = std::to_string(n);
    int size = number.size();

    if(size == 1)
        return -1;
    char temp = number[1];

    for(int i=0, m=number.size()-1; i<m; ++i)
    {
        if(number[i] > temp)
            return (m-i);
        temp = number[i+2];
    }
    return -1;

}

// subtract enough from number
int64_t subtract(int64_t n, int index)
{
    int64_t result = n;
    int64_t minus;
    //cout << "index " << index << endl;
    if(index == 0)
        return result-1;
    else
    {
        minus = n % (int64_t(pow(10, index)));
        if(minus == 0)
            minus = 1;
        //cout << "minus " << minus << endl;
    }

    return result -= minus;
}

bool isTidy(int64_t n)
{
    int next_digit = n%10;
    n /= 10;

    while(n)
    {
        int digit = n%10;

        if(digit > next_digit)
            return false;

        n /=10;
        next_digit = digit;
    }

    return true;
}

int main()
{
    int t;
    int64_t n;
    cin >> t;

    for(int i = 1; i <= t; ++i)
    {
        cin >> n;
        //cout << "number: "<< n << endl;
        int unsorted = index(n);
        //cout << "not sorted at " << unsorted << endl;

        while(!isTidy(n))
        {
            if (unsorted == 0)
            {
                n--;
                //cout << "one subtracted from" << n << endl;
                continue;
            }
            n = subtract(n, unsorted);
            unsorted = index(n);
            //cout << "unsorted index " << unsorted << endl;
        }
        cout << "Case #" << i << ": "<< n << endl;
    }

    return 0;
}
