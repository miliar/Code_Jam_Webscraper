#include <iostream>
using namespace std;

int main()
{
    int t, lastIndex, resetIndex, len;
    string str;
    cin>>t;
    for(int i = 0; i < t; i++)
    {
        cin>>str;
        lastIndex = str.length() - 1;
        len = resetIndex = str.length();
        for(int i = lastIndex - 1; i >= 0; i--)
        {
            if(str[i] > str[i + 1])
            {
                str[i] = str[i] - 1;
                resetIndex = i+1;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(str[0] != '0')
            cout<<str[0];
        for(int j = 1; j < resetIndex; j++)
            cout<<str[j];
        for(int j = resetIndex; j < len; j++)
            cout<<'9';
        cout<<endl;
    }
    return 0;
}
