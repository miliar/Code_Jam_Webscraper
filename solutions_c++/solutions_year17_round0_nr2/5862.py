#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen( "input.txt" ,"r", stdin );
    freopen( "output.txt", "w" ,stdout );
    long long t, l, len, n, i;
    cin >> t;
    for( l = 1; l <= t; l++ )
    {
        cin >> n;

        if( n < 10 )
        {
            cout << "Case #" << l << ": " << n <<endl;
            continue;
        }


        stringstream ss;
        ss << n;
        string str = ss.str();

        len = str.length();

        for( i = 0; i < len - 1; i++ )
        {
            if( str[i] > str[i + 1] )
            {
                str[i] = str[i] - 1;
                i++;
                for( i; i < len; i++ )
                    str[i] = '9';
                break;
            }
        }

        for( i = len - 1; i > 0; i-- )
        {
            if( str[i] < str[i - 1] )
            {
                str[i] = '9';
                str[ i - 1 ] = str[ i - 1 ] - 1;
            }
        }

        if( str[0] == '0' )
        {
            cout << "Case #" << l << ": ";
            for( i = 1; i < len; i++ )
                cout << str[i];
            cout << endl;
        }
        else
            cout << "Case #" << l << ": " << str <<endl;
    }
    return 0;
}
