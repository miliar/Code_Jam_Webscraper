// Example program
#include <iostream>
#include <string>
using namespace std;

int num;
string flip(string str, int index, int num)
{
    for(size_t i=index;i<index + num;i++)
    {
        if(str[i] == '-')
        {
            str[i] = '+';
        }
        else if(str[i] == '+')
            str[i] = '-';
    }
    return str;
}

int main()
{
    int T;
    cin >> T;
    string str;
    int k;
    bool is;
    for(int i=0;i<T;i++)
    {
        cin >> str >> k;
        num = 0;
        for(size_t j=0;j<str.length();j++)
        {
            if(str[j] == '-' && j + k  < str.length() + 1)
            {
                str = flip(str,j,k);
                num++;
            }
        }
        for(size_t j=0;j<str.length();j++)
        {
            if(str[j] == '+')
                is = true;
            else
            {
                is = false;
                break;
            }
        }
        if(is)
        {
            cout << "Case #" << i+1 << ": " << num << endl;
        }
        else
        {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

