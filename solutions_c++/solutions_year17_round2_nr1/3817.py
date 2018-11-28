#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main()
{
    int t;
    int num;
    cin >> t;
    num = t;
    while( t-- )
    {
        long long int d,dist, n; double maxtime = -1,remaining,speed;
        cin >> d >> n;

        for( int i = 0; i < n ; i++ )
        {
            cin >> dist >> speed;
            remaining = d - dist;
            if( remaining/speed > maxtime )
                maxtime = remaining/speed;
        }

        printf("Case #%d: %.6f\n",  num - t, d/maxtime);
    }
    return 0;
}
