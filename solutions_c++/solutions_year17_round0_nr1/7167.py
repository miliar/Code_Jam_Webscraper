#include <iostream>
#include <string>
using namespace std;

int main()
{
    long long int t;
    cin >> t;

    string s;

    for( long long int c = 1; c <= t; c++  )
    {
        long long int fSize = 0;
        long long int count = 0;
        long long int flag = 0;

        cin >> s;

        cin >> fSize;

        for(long long int i = 0; i < s.size(); i++  )
        {

            long long int k = 0;
            if( s[i] == '-' )
            {

                if( s.size() - i < fSize )
                {
                    cout<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<endl;
                    flag = 1;
                    break;
                }


                for(k = 0; k < fSize; k++ )
                {
                    if( s[i + k] == '-' )
                        s[i + k] = '+';
                    else
                        s[i + k] = '-';
                }

                count++;
            }

        }

         if( !flag )
            cout<<"Case #"<<c<<": "<<count<<endl;

       }





    return 0;
}
