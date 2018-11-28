#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    int array_n[20];
    long long n;
    cin >> t;
    for (int p=1; p<=t; p++)
    {
        int ans = 0;
        cin >> n;
        int num_n=1, copy__n=n;

        while (n>9)
        {
            array_n[num_n-1]=n%10;
            num_n++;
            n/=10;
        }
        array_n[num_n-1] = n;
        reverse(array_n, array_n + num_n);
        for (int i =num_n-1; i>0; i--)
        {
            if (array_n[i]<array_n[i-1])
            {
                int h=i;
                while ((h<num_n) && (array_n[h] != 9))
                {
                    array_n[h] = 9;
                    h++;
                }

                array_n[i-1] = array_n[i-1] -1;
            }

        }
        cout << "Case #" << p<< ": ";
        if (array_n[0] != 0) cout << array_n[0];
        for (int o=1; o<num_n; o++)
        cout << array_n[o];
        cout << endl;

    }
}
