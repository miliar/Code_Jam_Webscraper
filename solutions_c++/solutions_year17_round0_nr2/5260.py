#include <iostream>
#include <cmath>

using namespace std;

int dig(long int);

int main()
{
    int t;
    long int n;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cin >> n;
        int steps = 0;

        cout << "Case #" << i << ": ";

        int d = dig(n);
        if(d > 0)
        {
            long int mult = pow(10,d);
            n /= mult;
            long int low = n%10;
            n /= 10;
            n *= mult * 10;
            low *= mult;
            n += low - 1;
        }

        cout << n << endl;
    }
    return 0;
}

int dig(long int count)
{
    long int buff = count;
    int max_dig = 0;
    int idig = 0;
    int f_Ntidy = false;
    while(buff > 0)
    {
        int next = (buff/10)%10;
        int curr = buff % 10;

        if(next > curr)
        {
            f_Ntidy = true;
        }
        else if(f_Ntidy && next < curr)
        {
           max_dig = idig;
           f_Ntidy = false;
        }

        idig++;
        buff /=10;
    }

    return max_dig;
}
