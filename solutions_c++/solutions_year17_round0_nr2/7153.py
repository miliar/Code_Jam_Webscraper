#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    string s;

    cin>>n;

    for( int i = 0; i < n ; i++ )
    {
        cin >> s;
        long long int j = 0;
        long long int final_i = -1;
        for( j = s.size() - 1; j > 0; j-- )
        {

           if( s[j - 1] > s[j] || s[j - 1] == '0')
           {
              s[j - 1] = s[j - 1] - 1;
              s[j] = '9';
              final_i = j;
           }
        }

        if( s[0] == '0' )
        {
            s.erase(s.begin());
        }

        cout<<"Case #"<<i+1<<": ";
        if( final_i != -1 )
        {
            for( long long int i = 0; i < final_i; i++ )
            {
                cout<<s[i];
            }
            for( long long int i = final_i; i < s.size(); i++)
                cout<<'9';

            cout<<endl;
        }
        else
        {
            cout<<s<<endl;
        }


    }



    return 0;
}
