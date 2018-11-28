#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("BS.in", "r", stdin);
    freopen("BS.out", "w", stdout);
    int a[1000], j = 0;
    for(int i = 1; i <= 999; i++)
    {
        int x, y, z;
        x = i%10;
        y = (i%100)/10;
        z = i/100;
        if(x >= y && y >= z)
        {
            a[j] = i;
            j++;
        }
    }
    //for(int i = 0; i < 1000; i++) cout << a[i] << " ";
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        int n;
        cin >> n;
        for(int jj = 0; jj < 1000; jj++)
        {
            if(a[jj] > n)
            {
                cout << "Case #" << i << ": " << a[jj-1] << "\n";
                break;
            }
        }
    }
}
