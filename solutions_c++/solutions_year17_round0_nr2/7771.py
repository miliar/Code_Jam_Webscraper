#include <iostream>
#include <string>
using namespace std;
bool check(string inp, int size)
{
    int flag = 0;
    for(int i = 0; i < size-1; i++)
    {
        if(inp[i] > inp[i+1])
            flag = 1;
    }
    if(flag)
        return false;
    else    return true;
}
int main()
{
    int t,i,c=1;
    cin >> t;
    string inp;
    while(t--)
    {
        cin >> inp;
        int size = inp.size();
        while ( !check(inp,size))
        {
            for(i =0; i < size-1; i++)
            {
                if(inp[i] > inp[i+1])
                {
                    inp[i]--;
                    for(int k = i+1; k < size; k++)
                        inp[k] = '9';
                    break;
                }
            }
        }
        //Remove leading zeroes
        if(inp[0] == '0')
            inp = inp.substr(inp.find_first_not_of('0'),string::npos);
        cout << "Case #" << c<< ": " << inp << endl;
        c++;
    }
    return 0;
}
