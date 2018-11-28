#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r" , stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    for(int c = 1 ; c <= t ; c++)
    {
        string s;
        cin>>s;

        int k;
        cin>>k;

        int n = s.length();
        bool flag = 0;
        int Count = 0;

        for(int i = 0 ; i < n ; i++)
        {
            if(s[i] == '-')
            {
                Count++;
                int j = i;
                if( ( i + k) > n )
                {
                    flag = 1;
                    break;
                }
                while( j < ( i + k ))
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else if(s[j] == '+')
                        s[j] = '-';

                    j++;
                }
            }
        }

		cout<<"Case #"<<c<<": ";
        if( flag )
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<Count<<endl;

    }

    return 0;
}
