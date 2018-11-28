#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen( "input.txt" ,"r", stdin );
    freopen( "output.txt", "w" ,stdout );
    long long test, t;
    cin >> test;
    for( t = 1; t <= test; t++ )
    {
        double ans, des, num_h, i, d, sp, time, max_time, d_max, sp_max;
        max_time = -1;

        cin >> des >> num_h;
        for( i = 1; i <= num_h; i++ )
        {
            cin >> d >> sp;
            time = ( des - d ) / sp;
            if( max_time < time )
            {
                max_time = time;
                d_max = d;
                sp_max = sp;
            }
        }

        ans = ( ( des * sp_max ) / ( des - d_max ) ) ;

        cout << "Case #" << t << ": " << setprecision (6) << fixed << ans << endl;
    }
    return 0;
}
