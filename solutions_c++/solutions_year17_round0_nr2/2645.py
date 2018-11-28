#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long T;
    cin>>T;
    for(long long t = 1;t<=T;t++)
    {
        string s;
        cin>>s;
        long long len = s.length();
        for(long long i = len-1;i>0;i--)
        {
            if(s[i] < s[i-1])
            {
                if(s[i-1] == '0')
                    s[i-1] = '9';
                else
                s[i-1]--;
                s[i] = '9';
            }
        }
        for(long long i = 0;i< len-1;i++)
        {
            if(s[i] > s[i+1])
            {

                s[i+1] = '9';
            }
        }

                cout<<"Case #"<<t<<": ";
long long f = 0;
        for(long long i = 0;i< len;i++)
        {
            if(s[i]>'0')
                f = 1;
            if(f)
                cout<<s[i];
        }
        cout<<endl;

    }

}
