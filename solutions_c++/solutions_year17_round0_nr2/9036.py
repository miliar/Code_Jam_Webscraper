#include <iostream>

using namespace std;

int main()
{
    int t, x = 0;
    cin >> t;
    while(t--)
    {
        x++;
        long long n;
        cin >> n;
        long long m = n + 1;
        while(--m)
        {
            long long temp = m;
            int arr[10] = {0}, tidy;
            while(temp)
            {
                int i, r = temp % 10;
                temp /= 10;
                for(i = r - 1; i >= 0; i--)
                    if(arr[i])
                        break;

                if(i == -1)
                {
                    if(!temp)
                        tidy = 1;
                    arr[r]++;
                }
                else
                {
                    tidy = 0;
                    break;
                }
            }
            if(!tidy)
                continue;
            else
            {
                cout << "Case #" << x << ": " << m << endl;
                break;
            }
        }
    }
    return 0;
}

