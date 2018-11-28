#include <iostream>
using namespace std;
#define PRINT 0

void strrev(string &str, int &index, int &len)
{
    for(int i = index; i < index + len; i++)
    {
        str[i] = str[i] == '+' ? '-' : '+';
    }
}

int main()
{
    int t,k,len,ans;
    string str;
    bool impossible;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        cin>>str>>k;
        ans = 0;
        impossible = false;
        len = str.length();
        for(int index = 0; index < len; index++)
        {
            if(str[index] == '+')
            {
                continue;
            }
            else
            {
                if(len - index < k)
                {
                    impossible = true;
                    break;
                }
                #if PRINT
                cout<<"index : "<<index<<endl;
                cout<<"str before rev : "<<str<<endl;
                #endif
                strrev(str, index, k);
                #if PRINT
                cout<<"str after rev : "<<str<<endl;
                #endif
                ans++;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(impossible)
            cout<<"IMPOSSIBLE"<<endl;
        else 
            cout<<ans<<endl;
    }
    return 0;
}
