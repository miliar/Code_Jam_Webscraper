#include <iostream>
#include <cstring>
#include <cstdio>
#include <climits>
using namespace std;

int main()
{
    freopen("in2.in","r",stdin);
    freopen("ans2.txt","w",stdout);

    long long int t,k,flips,flag;
    string s;
    //char ch;
    cin>>t;
    for(long long int p = 1 ; p <=t ; ++p)
    {
        flips = 0;
        flag = 0;
        cin>>s;

        cin>>k;
        for(long long int i = 0 ; i <= s.length()-k; ++i)
        {
      //      cin>>ch;
            if(s.at(i) == '-')
            {
                for(long long int h = i ; h< i+k;++h)
                {
                    s.at(h)=(s.at(h)=='-')?'+':'-';
                }
                ++flips;
            }
        }
        for(long long int i = s.length()-k+1 ; i<s.length(); ++i )
        {
            if(s.at(i)=='-')
            {
                flag = 1;
            }
        }
        cout<<"Case #"<<p<<": ";
        if(flag == 1)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            cout<<flips<<endl;
        }
    }
    return 0;
}
