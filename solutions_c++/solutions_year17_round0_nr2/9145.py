#include <iostream>
#include <cmath>

typedef unsigned long long ULL;

using namespace std;

int num_digits(ULL num)
{
    int count = 0;
    while(num != 0)
    {
        num /= 10;
        count++;
    }
    return count;
}

bool if_tidy(ULL num)
{
    int prev = 9;
    int curr = 0;
    while(num != 0)
    {
        curr = num%10;
        num /= 10;
        if(curr > prev)
            return false;
        prev = curr;
    }
    return true;
}

int search(ULL num)
{
    ULL first_guess = pow(10, num_digits(num) - 1) - 1;
    while(!if_tidy(num) && num != first_guess)
    {
        num--;
    }
    return num;
}

int main()
{
    int T;
    cin >> T;

    ULL num;

    for(int i=0; i<T; i++)
    {
        cin >> num;
        cout << "Case #" << i + 1 << ": " << search(num) << endl;
    }
}

