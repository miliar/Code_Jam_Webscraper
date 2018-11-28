#include <iostream>
#include <algorithm>

using namespace std;

bool tidy(int n)
{
    int cmp = 10;
    while (n != 0)
    {
        int last = n % 10;
        if (last > cmp)
            return false;
        
        cmp = last;
        n /= 10;
    }

    return true;
}

int main()
{
    ios_base::sync_with_stdio(0);

    int tests;
    cin >> tests;

    for(int x=1; x <= tests; x++)
    {
        int n;
        cin >> n;
        
        cout << "Case #" << x << ": ";

        while(n >= 0)
        {
            if(tidy(n))
            {
                cout << n;
                break;
            }
            n--;
        }

        cout << "\n";

    }

    return 0;
}