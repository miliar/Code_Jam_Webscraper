#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen( "input.txt" ,"r", stdin );
    freopen( "output.txt", "w" ,stdout );
    int i, j, t, s, cnt, len, l;
    string str;
    cin >> t;
    for( l = 1; l <= t; l++ )
    {
        cin >> str;
        cin >> s;
        len = str.length();
        i = 0;
        cnt = 0;
        while( i < len )
        {
            if( str[i] == '-' )
            {
                cnt++;
                for( j = 0; j < s; j++ )
                {
                    if ( ( i + j ) < len )
                    {
                        if( str[i + j] == '-' )
                            str[i + j] = '+';
                        else
                            str[i + j] = '-';
                    }
                    else
                    {
                        str[len - 1] = '-';
                        break;
                    }
                }
            }
            i++;
        }
        cout << "Case #" << l << ": ";
        if( str[len-1] == '+' )
            cout << cnt << endl;
        else
            cout<< "IMPOSSIBLE\n";
    }
    return 0;
}
