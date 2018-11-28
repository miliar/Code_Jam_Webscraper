
#include <iostream>
#include <string>
using namespace std;

int num;
string flipper(string row, int index, int num)
{
    for(size_t i=index;i<index + num;i++)
    {
        if(row[i] == '-')
        {
            row[i] = '+';
        }
        else if(row[i] == '+')
            row[i] = '-';
    }
    return row;
}

int main()
{
    int T;
    cin >> T;
    string row;
    int k;
    bool happyside;
    for(int i=0;i<T;i++)
    {
        cin >> row >> k;
        num = 0;
        for(size_t j=0;j<row.length();j++)
        {
            if(row[j] == '-' && j + k  < row.length() + 1)
            {
                row = flipper(row,j,k);
                num++;
            }
        }
        for(size_t j=0;j<row.length();j++)
        {
            if(row[j] == '+')
                happyside = true;
            else
            {
                happyside = false;
                break;
            }
        }
        if(happyside)
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