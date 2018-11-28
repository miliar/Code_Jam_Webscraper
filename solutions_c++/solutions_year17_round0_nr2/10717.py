#include <iostream>

using namespace std;

int main()
{
    int t, i;
    cin >> t;
    int n[t], y[t];
    if(t >= 1 && t <= 100)
    {
        for(i = 0; i < t; i++)
            cin >> n[i];
        for(i = 0; i < t; i++)
        {
            z:
            if(n[i]%10 >= (n[i]/10)%10 && n[i]/100 <= (n[i]/10)%10)
                y[i] = n[i];
            else if(n[i] == 1000)
                y[i] = 999;
            else if((n[i]*10)%10 == n[i])
                y[i] = n[i];
            else
            {
                n[i] -= 1;
                goto z;
            }
        }
        for(i = 0; i < t; i++)
            cout << "Case #" << i+1 << ": " << y[i] << "\n";
    }
    return 0;
}
